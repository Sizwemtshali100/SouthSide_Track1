# Generated by Django 4.1.4 on 2023-03-16 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SouthsideApp', '0002_remove_qacmodels_kpa_outcome_qacmodels_kpa_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='qacmodels',
            name='Comment',
            field=models.TextField(default=True, max_length=200),
        ),
    ]