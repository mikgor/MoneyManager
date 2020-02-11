from django.contrib import admin
from django.urls import path
from MoneyManagerApp import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
    url('^dashboard/$', views.DashboardView.as_view(), name='DashboardView'),
    url('^dashboard/(?P<month>[0-9]+)/(?P<year>[0-9]+)/$', views.DashboardView.as_view(), name='DashboardView'),
    url(r'^signup/$', views.SignUpView.as_view(), name='SignupView'),
    url(r'^login/$', auth_views.LoginView.as_view(), name='LoginView'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='LogoutView'),
    url(r'accountcreate/$', views.AccountCreateView.as_view(), name='AccountCreateView'),
    url(r'transactioncreate/(?P<type>.+)/$', views.TransactionCreateView.as_view(), name='TransactionCreateView'),
    url(r'^(?P<pk>[0-9]+)/accountdelete/$', views.AccountDeleteView.as_view(), name='AccountDeleteView'),
    url(r'^(?P<pk>[0-9]+)/transactiondelete/$', views.TransactionDeleteView.as_view(), name='TransactionDeleteView'),
    path('admin/', admin.site.urls),
]
