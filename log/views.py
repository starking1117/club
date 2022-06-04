from django.shortcuts import render
from django.views.generic import *
from django.urls import reverse
from .models import FormItem,ClubItem
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

class FormCreate(PermissionRequiredMixin,CreateView):
  model = FormItem
  permission_required = 'log.add_formitem'
  fields = ['stu_name', 'stu_grade', 'stu_class', 'stu_num','ori_club','new_club','note']

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

class FormReply(PermissionRequiredMixin,UpdateView):
  model = FormItem
  permission_required = 'log.change_formreply'

  