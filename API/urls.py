from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserList, name='user_list_view'),
]
