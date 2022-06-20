from re import U
from urllib import request
from django.shortcuts import render
from django.views.generic import *
from django.urls import reverse
from .models import TransferForm,ClubItem,Profile
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q

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
    def get_queryset(self):
      if self.request.user.groups.filter(name='教務處人員').exists():
        return TransferForm.objects.all()
      direct_club = self.request.user.direct_club.all()[:1]
      tutor_club = self.request.user.tutor_club.all()[:1]
      return TransferForm.objects.filter(
        Q(club_orig__in=direct_club,approve_od=0) |
        Q(club_orig__in=tutor_club,approve_od=1,approve_oa=0) |
        Q(club_new__in=direct_club,approve_oa=1,approve_nd=0) |
        Q(club_new__in=tutor_club,approve_nd=1,approve_na=0)  
      )


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
  
  def get_form(self):
    form = super().get_form()
    rec = self.object
    if rec.approve_od == 0 :
      unwant_fields = [ 'user','club_new','club_orig','approve_oa', 'approve_nd', 'approve_na', 'approve_st', 'note_stu' , 'note_oa']
      for field in unwant_fields:
        del form.fields[field]
    elif rec.approve_oa == 0 :
      unwant_fields = [ 'user','club_new','club_orig','approve_od', 'approve_nd', 'approve_na', 'approve_st', 'note_od','note_stu']
      for field in unwant_fields:
        del form.fields[field]
    elif rec.approve_nd == 0 :
      unwant_fields = [ 'user','club_new','club_orig','approve_od', 'approve_oa', 'approve_na', 'approve_st', 'note_od', 'note_stu' , 'note_oa']
      for field in unwant_fields:
        del form.fields[field]
    elif rec.approve_na == 0 :
      unwant_fields = [ 'user','club_new','club_orig','approve_od', 'approve_nd', 'approve_oa', 'approve_st', 'note_od' ,'note_stu', 'note_oa']
      for field in unwant_fields:
        del form.fields[field]
    elif rec.approve_na == 1 :
      unwant_fields = [ 'user','club_new','club_orig','approve_od', 'approve_nd', 'approve_oa', 'approve_na', 'note_od' ,'note_stu', 'note_oa']
      for field in unwant_fields:
        del form.fields[field]
    return form

  def get_success_url(self):
   return reverse('form_list')


  