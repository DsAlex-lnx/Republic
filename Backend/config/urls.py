from django.contrib import admin
from django.urls import path, include
from knox import views as knox_views

from rest_framework import routers
from studenthousing.api import viewsets
from studenthousing.views import login_api, get_user_data

route = routers.DefaultRouter()

route.register(r'users', viewsets.UserViewset, basename='Users')
route.register(r'republics', viewsets.RepublicsViewset, basename='Republics')
route.register(r'address', viewsets.AddressViewset, basename='Address')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',  login_api),
    path('user_data/',  get_user_data),
    path('logout/',  knox_views.LogoutView.as_view()),
    path('logout_all/',  knox_views.LogoutAllView.as_view()),
    path('', include(route.urls))
]
