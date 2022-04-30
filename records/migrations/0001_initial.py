# Generated by Django 4.0.3 on 2022-04-30 07:14

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mainAPP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('captain', models.ForeignKey(on_delete=django.db.models.expressions.Case, related_name='captain', to='mainAPP.player')),
                ('player1', models.ForeignKey(on_delete=django.db.models.expressions.Case, related_name='player1', to='mainAPP.player')),
                ('player10', models.ForeignKey(on_delete=django.db.models.expressions.Case, related_name='player10', to='mainAPP.player')),
                ('player11', models.ForeignKey(on_delete=django.db.models.expressions.Case, related_name='player11', to='mainAPP.player')),
                ('player2', models.ForeignKey(on_delete=django.db.models.expressions.Case, related_name='player2', to='mainAPP.player')),
                ('player3', models.ForeignKey(on_delete=django.db.models.expressions.Case, related_name='player3', to='mainAPP.player')),
                ('player4', models.ForeignKey(on_delete=django.db.models.expressions.Case, related_name='player4', to='mainAPP.player')),
                ('player5', models.ForeignKey(on_delete=django.db.models.expressions.Case, related_name='player5', to='mainAPP.player')),
                ('player6', models.ForeignKey(on_delete=django.db.models.expressions.Case, related_name='player6', to='mainAPP.player')),
                ('player7', models.ForeignKey(on_delete=django.db.models.expressions.Case, related_name='player7', to='mainAPP.player')),
                ('player8', models.ForeignKey(on_delete=django.db.models.expressions.Case, related_name='player8', to='mainAPP.player')),
                ('player9', models.ForeignKey(on_delete=django.db.models.expressions.Case, related_name='player9', to='mainAPP.player')),
                ('vice_captain', models.ForeignKey(on_delete=django.db.models.expressions.Case, related_name='vice_captain', to='mainAPP.player')),
            ],
        ),
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_fee', models.FloatField(default=1)),
                ('length', models.IntegerField(default=1)),
                ('price_fee', models.FloatField(default=0)),
                ('teams', models.ManyToManyField(to='records.userteam')),
            ],
        ),
    ]
