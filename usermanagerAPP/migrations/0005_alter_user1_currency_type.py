# Generated by Django 4.0.3 on 2022-04-30 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagerAPP', '0004_alter_user1_currency_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user1',
            name='currency_type',
            field=models.CharField(choices=[('vision candies', 'vision candies'), ('vision coins', 'vision coins')], default='vision candies', max_length=50),
        ),
    ]
