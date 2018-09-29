from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from frontend import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('frontend.urls'))
]
