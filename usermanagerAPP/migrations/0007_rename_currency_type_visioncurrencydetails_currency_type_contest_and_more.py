# Generated by Django 4.0.3 on 2022-05-17 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagerAPP', '0006_visioncurrencydetails'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visioncurrencydetails',
            old_name='currency_type',
            new_name='currency_type_contest',
        ),
        migrations.AddField(
            model_name='visioncurrencydetails',
            name='currency_type_user',
            field=models.CharField(default='vision candies', max_length=20),
        ),
    ]
