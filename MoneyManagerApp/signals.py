from .models import Account, Transaction
from django.db.models import signals
from django.db.models.signals import post_save
import datetime

def account_saved(sender, instance, created, **kwargs):
    if created and instance.balance > 0.00:
        Transaction.objects.create(account=instance, date=datetime.datetime.now(), category='Initial balance', value=instance.balance, type='N')

def transaction_saved(sender, instance, created, **kwargs):
    if created and instance.type != 'N':
        instance.account.set_balance(instance)


post_save.connect(account_saved, sender=Account)
post_save.connect(transaction_saved, sender=Transaction)
