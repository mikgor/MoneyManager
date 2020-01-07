from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

class Currency(models.Model):
    name = models.CharField(_('Currency name'), max_length=20)
    short_name = models.CharField(_('Currency short name'), max_length=3)
    symbol = models.CharField(_('Currency sign'), max_length=1)
    # if true then display symbol before number for ex. $4 otherwise display symbol after 4€
    prefix = models.BooleanField(_('Prefix'), default=False)

class User(AbstractUser):
    pass

    def __str__(self):
        return self.email

class Account(models.Model):
    name = models.CharField(_('Account name'), max_length=10)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='accounts')
    balance = models.DecimalField(_('Value'), max_digits=8, decimal_places=2)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    BANKACCOUNT = 'BA'
    CASH = 'CH'
    CARD = 'CD'
    ACCOUNT_TYPE_CHOICES = (
        (BANKACCOUNT, _('Bank account')),
        (CASH, _('Cash')),
        (CARD, _('Card')),
    )
    type = models.CharField(_('Account type'), max_length=2, choices=ACCOUNT_TYPE_CHOICES, default=BANKACCOUNT)

    def print_balance(self):
        return '%s %d' % (self.currency.symbol, self.balance) if self.currency.prefix else '%d %s' % (self.balance, self.currency.symbol)

    def set_balance(self, transaction):
        if transaction.account.id == self.id:
            self.balance += transaction.value
            self.save()

class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='transactions')
    date = models.DateTimeField(_('Transaction date'))
    category = models.CharField(_('Transaction category'), max_length=15)
    value = models.DecimalField(_('Transaction value'), max_digits=8, decimal_places=2)
    details = models.CharField(_('Transaction details'), max_length=25)
    INCOME = 'I'
    OUTCOME = 'O'
    TRANSACTION_TYPE_CHOICES = (
        (INCOME, _('Income')),
        (OUTCOME, _('Outcome')),
    )
    type = models.CharField(_('Transaction type'), max_length=1, choices=TRANSACTION_TYPE_CHOICES)
