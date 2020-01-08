# Generated by Django 2.0.7 on 2020-01-08 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MoneyManagerApp', '0002_auto_20200107_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='balance',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Balance'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='type',
            field=models.CharField(choices=[('I', 'Income'), ('O', 'Outcome'), ('N', 'Initial')], max_length=1, verbose_name='Transaction type'),
        ),
    ]
