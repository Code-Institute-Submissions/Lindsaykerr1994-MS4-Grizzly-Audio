# Generated by Django 3.0.8 on 2020-08-18 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20200814_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='default_county',
            field=models.CharField(default=' ', max_length=40),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='default_phone_number',
            field=models.CharField(default=' ', max_length=20),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='default_post_code',
            field=models.CharField(default=' ', max_length=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='default_street_address1',
            field=models.CharField(default=' ', max_length=80),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='default_street_address2',
            field=models.CharField(default=' ', max_length=80),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='default_town_or_city',
            field=models.CharField(default=' ', max_length=40),
        ),
    ]