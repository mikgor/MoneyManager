from django.contrib import admin
from django.urls import path
from MoneyManagerApp import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
    url('^dashboard/$', views.DashboardView.as_view(), name='DashboardView'),
    url(r'^signup/$', views.SignUpView.as_view(), name='SignupView'),
    url(r'^login/$', auth_views.LoginView.as_view(), name='LoginView'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='LogoutView'),
    url(r'accountcreate/$', views.AccountCreateView.as_view(), name='AccountCreateView'),
    url(r'transactioncreate/$', views.TransactionCreateView.as_view(), name='TransactionCreateView'),
    path('admin/', admin.site.urls),
]
