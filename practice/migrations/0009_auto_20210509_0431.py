# Generated by Django 3.1.7 on 2021-05-09 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0008_user_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='email',
            field=models.CharField(max_length=100),
        ),
    ]
