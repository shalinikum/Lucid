# Generated by Django 3.1.7 on 2021-05-09 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0006_auto_20210509_0420'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='use_rname',
        ),
    ]
