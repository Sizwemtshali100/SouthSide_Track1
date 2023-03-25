# Generated by Django 4.1.4 on 2023-03-20 00:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SouthsideApp', '0008_remove_qacmodels_user_qacmodels_qa_agent'),
    ]

    operations = [
        migrations.AddField(
            model_name='qaagent',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
