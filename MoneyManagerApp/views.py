from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import *
from .forms import *
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from django.conf import settings
from django.http import Http404

class LoginRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return HttpResponseRedirect(reverse_lazy(settings.LOGIN_URL))
        return super().dispatch(request, *args, **kwargs)

class DashboardView(LoginRequiredMixin, generic.ListView):
    template_name = 'moneymanagerapp/dashboard.html'
    context_object_name = 'account_list'
    queryset = ''

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        accounts = self.request.user.accounts.all()
        context['account_list'] = accounts
        context['transactions'] = None
        id = self.kwargs.get('account_id', None)
        if id is None:
            kwargs.update({'account_id': accounts.first().id})
            id = self.kwargs.get('account_id', None)
        if accounts.filter(id=id).exists():
            context['transactions'] = accounts.get(id=id).transactions.order_by('-date')#.filter(date__month=1)
        return context

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('LoginView')
    template_name = 'registration/signup.html'

class AccountCreateView(LoginRequiredMixin, CreateView):
    form_class = AccountCreationForm
    template_name = 'moneymanagerapp/account_form.html'
    success_url = reverse_lazy('DashboardView')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class AccountDeleteView(LoginRequiredMixin, DeleteView):
    model = Account
    success_url = reverse_lazy('DashboardView')

    def get_object(self, queryset=None):
        object = super(AccountDeleteView, self).get_object()
        if not object.owner == self.request.user:
            raise Http404
        return object

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.owner == request.user:
            self.object.delete()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(reverse_lazy('DashboardView'))

class TransactionDeleteView(LoginRequiredMixin, DeleteView):
    model = Transaction
    success_url = reverse_lazy('DashboardView')

    def get_object(self, queryset=None):
        object = super(TransactionDeleteView, self).get_object()
        if not object.account.owner == self.request.user:
            raise Http404
        return object

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.account.owner == request.user:
            self.object.delete()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(reverse_lazy('DashboardView'))

class TransactionCreateView(LoginRequiredMixin, CreateView):
    form_class = TransactionCreationForm
    template_name = 'moneymanagerapp/transaction_form.html'
    success_url = reverse_lazy('DashboardView')

    def get_form(self, *args, **kwargs):
        form = super(TransactionCreateView, self).get_form(*args, **kwargs)
        form.fields['account'].queryset = self.request.user.accounts
        return form

    def get_form_kwargs(self):
        kwargs = super(TransactionCreateView, self).get_form_kwargs()
        transaction_type = self.kwargs.get('type', None)
        if transaction_type is None or transaction_type not in ['income', 'outcome']:
            transaction_type = 'income'
        kwargs.update({'transaction_type': transaction_type})
        return kwargs

    def form_valid(self, form):
        self.object = form.save(commit=False)
        transaction_type = self.kwargs.get('type', None)
        if transaction_type is None or transaction_type not in ['income', 'outcome']:
            transaction_type = 'income'
        if transaction_type == 'income':
            self.object.type = 'I'
        elif transaction_type == 'outcome':
            self.object.type ='O'
        else:
            pass
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
