# Generated by Django 4.1.4 on 2023-03-26 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SouthsideApp', '0010_alter_qacmodels_qa_agent_delete_qaagent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qacmodels',
            name='KPA',
            field=models.CharField(choices=[('Product', 'Product'), ('Pass', 'Pass'), ('Compliance', 'Compliance'), ('Data Capturing', 'Data Capturing'), ('TCF', 'TCF')], default=False, max_length=15),
        ),
    ]
