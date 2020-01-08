from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, Account, Transaction

class UserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')

class AccountCreationForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ('name', 'balance', 'currency', 'type')

class TransactionCreationForm(forms.ModelForm):

    class Meta:
        model = Transaction
        fields = ('account', 'date', 'category', 'value', 'details')
