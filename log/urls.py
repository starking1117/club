from django.urls import path
from .views import *

urlpatterns = [
    path('', ClubList.as_view(), name='club_list'),
    path('<int:pk>/', ClubView.as_view(), name='club_view'),
    path('club_create/',ClubCreate.as_view(),name='club_create'),
    path('form_create/', FormCreate.as_view(), name='form_create'),
    path('<int:pk>/reply/', FormReply.as_view(), name='form_reply'),
]