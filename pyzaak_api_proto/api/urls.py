from django.urls import path
from rest_framework.documentation import include_docs_urls
from django.views.generic.base import RedirectView
from rest_framework_swagger.views import get_swagger_view
from . import views

urlpatterns = [
    path('users',
         views.UserList.as_view(),
         name='user_list'),

    path('user/<str:username>',
         views.UserDetail.as_view(),
         name='user_detail'),

    path('games',
         views.GameList.as_view(),
         name='game_list'),

    path('deck/<int:user>',
         views.SideDeckDetail.as_view(),
         name='side_deck_detail'
         ),

    path('docs',
         get_swagger_view(title='Pyzaak API Prototype'),
         name='docs'),

    path('', RedirectView.as_view(url='docs', permanent=True)),
]
