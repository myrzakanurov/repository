# Generated by Django 3.0.3 on 2020-02-24 12:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('repo', '0007_auto_20200224_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='upload_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]