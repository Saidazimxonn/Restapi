# Generated by Django 3.1.3 on 2021-03-29 10:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookcategory',
            name='company_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookcategory',
            name='email',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookcategory',
            name='phone',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
