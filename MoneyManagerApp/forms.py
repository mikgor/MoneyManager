from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, Account, Transaction
from MoneyManager.settings import INCOME_CATEGORY_CHOICES, OUTCOME_CATEGORY_CHOICES

class UserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')

class AccountCreationForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ('name', 'balance', 'currency', 'type')

class TransactionCreationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        transaction_type = kwargs.pop('transaction_type', None)
        super(TransactionCreationForm, self).__init__(*args, **kwargs)
        choices = INCOME_CATEGORY_CHOICES[1:] if transaction_type=='income' else OUTCOME_CATEGORY_CHOICES
        self.fields['category'] =  forms.ChoiceField(choices=choices)

    class Meta:
        model = Transaction
        fields = ('account', 'date', 'category', 'amount', 'details')
