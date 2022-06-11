from django.shortcuts import render
from django.views.generic import *
from django.urls import reverse
from .models import TransferForm,ClubItem
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin

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

  def get_initial(self):
    data = {}
    # 取得目前登入的使用者資訊
    u = self.request.user
    # 如果有名字，就填名字，否則就填帳號名稱
    if u.username:
      data['stu_name'] = u.username
    else:
      data['stu_name'] = u.first_name
    return data

  def get_success_url(self):
    return reverse('club_list')

class FormView(LoginRequiredMixin,DetailView):
  model = TransferForm

class FormReply(LoginRequiredMixin,UpdateView):
  model = TransferForm
  permission_required = 'log.add_clubitem'
  template_name = 'log/transferform_form.html'
  fields = ['approve_od','approve_oa','approve_nd','approve_na','approve_st','note_od','note_oa']
  def get_initial(self):
    data = {}
    # 取得目前登入的使用者資訊
    u = self.request.user
    # 如果有名字，就填名字，否則就填帳號名稱
    if u.username:
      data['stu_name'] = u.username
    else:
      data['stu_name'] = u.first_name
    return data
  def get_success_url(self):
    return reverse('form_list')

  