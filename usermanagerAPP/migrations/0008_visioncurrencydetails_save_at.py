# Generated by Django 4.0.3 on 2022-05-17 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagerAPP', '0007_rename_currency_type_visioncurrencydetails_currency_type_contest_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='visioncurrencydetails',
            name='save_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
