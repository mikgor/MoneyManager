from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import *
from .forms import *
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect


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
    success_url = reverse_lazy('LoginView')
    template_name = 'registration/signup.html'

class AccountCreateView(CreateView):
    form_class = AccountCreationForm
    template_name = 'moneymanagerapp/account_form.html'
    success_url = reverse_lazy('DashboardView')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class TransactionCreateView(CreateView):
    form_class = TransactionCreationForm
    template_name = 'moneymanagerapp/transaction_form.html'
    success_url = reverse_lazy('DashboardView')
