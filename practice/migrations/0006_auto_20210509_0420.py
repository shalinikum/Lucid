# Generated by Django 3.1.7 on 2021-05-09 04:20

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0005_auto_20210506_0639'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='use_rname',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='word',
            name='attribute',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='practice.wordsattribute'),
        ),
        migrations.AlterField(
            model_name='word',
            name='audio_file',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='word',
            name='illustration_video',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='word',
            name='image',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='wordsattribute',
            name='illustration_video',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]