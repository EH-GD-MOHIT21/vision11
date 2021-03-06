# Generated by Django 4.0.3 on 2022-06-11 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainAPP', '0004_alter_contest_teams_alter_contest_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='is_test_match',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='match',
            name='match_pause_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
