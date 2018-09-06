from django.urls import path
from . import views

urlpatterns = [
    path('users', views.UserList.as_view(), name='user_list'),
    path('user/<int:id>', views.UserDetail.as_view(), name='user_detail'),
    path('games', views.GameList.as_view(), name='game_list'),
    path(
        'deck/<int:user>',
        views.SideDeckDetail.as_view(),
        name='side_deck_detail'
        )
]
