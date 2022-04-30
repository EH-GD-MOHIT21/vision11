# Generated by Django 4.0.3 on 2022-04-30 05:55

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('mainAPP', '0001_initial'),
        ('records', '0002_alter_player_player_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userteam',
            name='captain',
            field=models.ForeignKey(on_delete=django.db.models.expressions.Case, related_name='captain', to='mainAPP.player'),
        ),
        migrations.AlterField(
            model_name='userteam',
            name='player1',
            field=models.ForeignKey(on_delete=django.db.models.expressions.Case, related_name='player1', to='mainAPP.player'),
        ),
        migrations.AlterField(
            model_name='userteam',
            name='player10',
            field=models.ForeignKey(on_delete=django.db.models.expressions.Case, related_name='player10', to='mainAPP.player'),
        ),
        migrations.AlterField(
            model_name='userteam',
            name='player11',
            field=models.ForeignKey(on_delete=django.db.models.expressions.Case, related_name='player11', to='mainAPP.player'),
        ),
        migrations.AlterField(
            model_name='userteam',
            name='player2',
            field=models.ForeignKey(on_delete=django.db.models.expressions.Case, related_name='player2', to='mainAPP.player'),
        ),
        migrations.AlterField(
            model_name='userteam',
            name='player3',
            field=models.ForeignKey(on_delete=django.db.models.expressions.Case, related_name='player3', to='mainAPP.player'),
        ),
        migrations.AlterField(
            model_name='userteam',
            name='player4',
            field=models.ForeignKey(on_delete=django.db.models.expressions.Case, related_name='player4', to='mainAPP.player'),
        ),
        migrations.AlterField(
            model_name='userteam',
            name='player5',
            field=models.ForeignKey(on_delete=django.db.models.expressions.Case, related_name='player5', to='mainAPP.player'),
        ),
        migrations.AlterField(
            model_name='userteam',
            name='player6',
            field=models.ForeignKey(on_delete=django.db.models.expressions.Case, related_name='player6', to='mainAPP.player'),
        ),
        migrations.AlterField(
            model_name='userteam',
            name='player7',
            field=models.ForeignKey(on_delete=django.db.models.expressions.Case, related_name='player7', to='mainAPP.player'),
        ),
        migrations.AlterField(
            model_name='userteam',
            name='player8',
            field=models.ForeignKey(on_delete=django.db.models.expressions.Case, related_name='player8', to='mainAPP.player'),
        ),
        migrations.AlterField(
            model_name='userteam',
            name='player9',
            field=models.ForeignKey(on_delete=django.db.models.expressions.Case, related_name='player9', to='mainAPP.player'),
        ),
        migrations.AlterField(
            model_name='userteam',
            name='vice_captain',
            field=models.ForeignKey(on_delete=django.db.models.expressions.Case, related_name='vice_captain', to='mainAPP.player'),
        ),
        migrations.DeleteModel(
            name='Player',
        ),
        migrations.DeleteModel(
            name='Team',
        ),
    ]
