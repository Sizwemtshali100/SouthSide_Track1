# Generated by Django 4.1.4 on 2023-03-19 22:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SouthsideApp', '0006_remove_qacmodels_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qacmodels',
            name='QA_Agent',
        ),
        migrations.AddField(
            model_name='qacmodels',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
