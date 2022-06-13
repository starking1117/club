from re import U
from urllib import request
from django.shortcuts import render
from django.views.generic import *
from django.urls import reverse
from .models import TransferForm,ClubItem
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.contrib.auth.models import User

class ClubList(ListView):
    model = ClubItem

class ClubView(LoginRequiredMixin,DetailView):
  model = ClubItem

class ClubCreate(PermissionRequiredMixin,CreateView):
  model = ClubItem
  permission_required = 'log.add_clubitem'
  fields = '__all__'
  def get_success_url(self):
    return reverse('club_view', kwargs={'pk': self.object.id})

class FormList(ListView):
    model = TransferForm

class FormCreate(PermissionRequiredMixin,CreateView):
  model = TransferForm
  permission_required = 'log.add_transferform'
  fields = '__all__'
  def get_form(self):
    form = super().get_form()
    # 把不要顯示的欄位從表單裡拿掉
    unwant_fields = [ 'user','approve_od', 'approve_oa', 'approve_nd', 'approve_na', 'approve_st', 'note_od', 'note_oa']
    for field in unwant_fields:
      del form.fields[field]
    return form

  def form_valid(self, form):
    form.instance.user = User.objects.get(id=self.request.user.id)
    return super().form_valid(form)

  def get_success_url(self):
    return reverse('club_list')

class FormView(LoginRequiredMixin,DetailView):
  model = TransferForm

class FormReply(LoginRequiredMixin,UpdateView):
  model = TransferForm
  permission_required = 'log.change_transferform'
  template_name = 'log/transferform_form.html'
  fields = '__all__'
  def get_initial(self):
    if TransferForm.approve_od == 0 :
      form = super().get_form()
      unwant_fields = [ 'user','approve_od', 'approve_oa', 'approve_nd', 'approve_na', 'approve_st', 'note_od', 'note_oa']
      for field in unwant_fields:
        del form.fields[field]
      return form



  def get_success_url(self):
   return reverse('form_list')

  