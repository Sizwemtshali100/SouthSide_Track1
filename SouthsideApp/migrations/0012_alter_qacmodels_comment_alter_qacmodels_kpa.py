# Generated by Django 4.1.4 on 2023-03-26 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SouthsideApp', '0011_alter_qacmodels_kpa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qacmodels',
            name='Comment',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='qacmodels',
            name='KPA',
            field=models.CharField(choices=[('Product', 'Product'), ('Pass', 'Pass'), ('Compliance', 'Compliance'), ('Data Capturing', 'Data Capturing'), ('TCF', 'TCF')], max_length=15),
        ),
    ]
