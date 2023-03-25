# Generated by Django 4.1.4 on 2023-03-16 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SouthsideApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qacmodels',
            name='KPA_Outcome',
        ),
        migrations.AddField(
            model_name='qacmodels',
            name='KPA',
            field=models.CharField(choices=[('Product', 'Product'), ('Pass', 'Pass'), ('Compliance', 'Compliance'), ('Data Capturing', 'Data Capturing'), ('TCF', 'TCF')], default=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='qacmodels',
            name='HIV_Required',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], max_length=3),
        ),
    ]