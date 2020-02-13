from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from MoneyManager.settings import INCOME_CATEGORY_CHOICES, OUTCOME_CATEGORY_CHOICES

class Currency(models.Model):
    name = models.CharField(_('Currency name'), max_length=20)
    short_name = models.CharField(_('Currency short name'), max_length=3)
    symbol = models.CharField(_('Currency sign'), max_length=3)
    # if true then display symbol before number for ex. $4 otherwise display symbol after 4€
    prefix = models.BooleanField(_('Prefix'), default=False)

    def __str__(self):
        return '%s (%s)' % (self.name, self.symbol)

class User(AbstractUser):
    pass

    def __str__(self):
        return self.email

class Account(models.Model):
    name = models.CharField(_('Account name'), max_length=10)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='accounts')
    balance = models.DecimalField(_('Balance'), max_digits=8, decimal_places=2)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, default='')
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
        return '%s%.2f' % (self.currency.symbol, self.balance) if self.currency.prefix else '%.2f%s' % (self.balance, self.currency.symbol)

    def set_balance(self, transaction):
        if transaction.account.id == self.id:
            type = transaction.type
            if type == 'I':
                self.balance += transaction.amount
            elif type == 'O':
                self.balance -= transaction.amount
            else:
                pass
            self.save()

    def set_balance_transaction_deleted(self, transaction):
        if transaction.account.id == self.id:
            type = transaction.type
            if type == 'I':
                self.balance -= transaction.amount
            elif type == 'O':
                self.balance += transaction.amount
            else:
                pass
            self.save()

    def __str__(self):
        return '%s (%s)' % (self.name, self.print_balance())

class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='transactions', default='')
    amount = models.DecimalField(_('Amount'), max_digits=8, decimal_places=2, validators=[MinValueValidator(0.00)])
    date = models.DateTimeField(_('Date'))
    details = models.CharField(_('Details'), max_length=25, blank=True, null=True)
    category = models.CharField(_('Category'), max_length=3, choices=INCOME_CATEGORY_CHOICES+OUTCOME_CATEGORY_CHOICES)
    INCOME = 'I'
    OUTCOME = 'O'
    TRANSACTION_TYPE_CHOICES = (
        (INCOME, _('Income')),
        (OUTCOME, _('Outcome')),
    )
    type = models.CharField(_('Transaction type'), max_length=1, choices=TRANSACTION_TYPE_CHOICES)

    def print_value(self):
        currency = self.account.currency
        return '%s%.2f' % (currency.symbol, self.amount) if currency.prefix else '%.2f%s' % (self.amount, currency.symbol)
