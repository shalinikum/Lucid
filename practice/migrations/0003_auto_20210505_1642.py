# Generated by Django 3.1.7 on 2021-05-05 16:42

from django.db import migrations


class Migration(migrations.Migration):
    
    atomic = False
    dependencies = [
        ('practice', '0002_auto_20210505_1622'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Doctors',
            new_name='Doctor',
        ),
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
    ]
