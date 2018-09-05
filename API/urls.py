from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserList.as_view(), name='user_list'),
    path('user/<int:id>', views.UserDetail.as_view(), name='user_detail')
]
