# Generated by Django 3.0.3 on 2020-02-24 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repo', '0006_auto_20200224_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='data_file',
            field=models.FileField(upload_to='documents'),
        ),
    ]
