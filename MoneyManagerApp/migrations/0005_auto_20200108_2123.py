# Generated by Django 2.0.7 on 2020-01-08 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MoneyManagerApp', '0004_auto_20200108_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='currency',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='MoneyManagerApp.Currency'),
        ),
    ]
