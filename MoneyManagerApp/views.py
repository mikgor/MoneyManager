from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import *
from .forms import *
from django.urls import reverse_lazy, reverse

class DashboardView(generic.ListView):
    template_name = 'moneymanagerapp/dashboard.html'
    context_object_name = 'account_list'
    queryset = ''

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['account_list'] = self.request.user.accounts.all()
        return context

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
