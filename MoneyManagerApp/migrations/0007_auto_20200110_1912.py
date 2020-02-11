# Generated by Django 2.0.7 on 2020-01-10 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MoneyManagerApp', '0006_auto_20200110_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='category',
            field=models.CharField(choices=[('IIL', 'Initial'), ('ISY', 'Salary'), ('IPN', 'Pension'), ('IBS', 'Bonds'), ('IDS', 'Dividends'), ('IGT', 'Grant'), ('IIT', 'Interest'), ('IOF', 'Offer'), ('IPE', 'Prize'), ('IRD', 'Refund'), ('IRL', 'Rental'), ('ISE', 'Sale'), ('ITR', 'Transfer'), ('IOR', 'Other'), ('OFD', 'Food'), ('OHD', 'Household'), ('OAL', 'Apparel'), ('OCE', 'Culture'), ('OEN', 'Education'), ('OES', 'Electronics'), ('OHH', 'Health'), ('OIT', 'Installment'), ('OLN', 'Loan'), ('OHY', 'Hobby'), ('OTT', 'Transportation'), ('OTR', 'Transfer'), ('OOR', 'Other')], max_length=3, verbose_name='Category'),
        ),
    ]
