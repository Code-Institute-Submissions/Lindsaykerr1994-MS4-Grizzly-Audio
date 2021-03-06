# Generated by Django 3.0.8 on 2020-10-17 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20201017_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='default_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='default_full_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
