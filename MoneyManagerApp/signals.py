from .models import Account, Transaction
from django.db.models import signals
from django.db.models.signals import post_save, post_delete
import datetime

def account_saved(sender, instance, created, **kwargs):
    if created and instance.balance > 0.00:
        Transaction.objects.create(account=instance, date=datetime.datetime.now(), amount=instance.balance, category='IIL', type='I')

def transaction_saved(sender, instance, created, **kwargs):
    if created and instance.category != 'IIL':
        instance.account.set_balance(instance)

def transaction_deleted(sender, instance, **kwargs):
    instance.account.set_balance_transaction_deleted(instance)

post_save.connect(account_saved, sender=Account)
post_save.connect(transaction_saved, sender=Transaction)
post_delete.connect(transaction_deleted, sender=Transaction)
