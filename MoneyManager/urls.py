from django.contrib import admin
from django.urls import path
from MoneyManagerApp import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
    url('^dashboard/$', views.DashboardView.as_view(), name='dashboard'),
    url(r'^signup/$', views.SignUpView.as_view(), name='signup'),
    url(r'^login/$', auth_views.LoginView.as_view(), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
]
