# Generated by Django 4.0.3 on 2022-03-17 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagerAPP', '0005_auto_20220315_2328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user1',
            name='second_name',
        ),
        migrations.AlterField(
            model_name='user1',
            name='last_name',
            field=models.CharField(max_length=20),
        ),
    ]