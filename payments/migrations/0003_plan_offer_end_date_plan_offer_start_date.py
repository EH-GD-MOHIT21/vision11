# Generated by Django 4.0.3 on 2022-04-01 10:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_rename_plans_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='offer_end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='plan',
            name='offer_start_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 1, 10, 8, 51, 318310, tzinfo=utc)),
        ),
    ]
