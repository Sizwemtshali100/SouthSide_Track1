# Generated by Django 4.1.4 on 2023-03-19 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SouthsideApp', '0004_qacagent_qacmodels_user_alter_qacmodels_avs_check'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='QACAgent',
            new_name='QAAgent',
        ),
        migrations.AddField(
            model_name='qacmodels',
            name='QA_Agent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='SouthsideApp.qaagent'),
        ),
    ]
