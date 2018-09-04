from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserList.as_view(), name='user_list_view'),
]
