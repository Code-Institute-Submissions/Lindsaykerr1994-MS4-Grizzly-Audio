# Generated by Django 3.0.8 on 2020-08-10 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('packs', '0004_pack_reduction'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pack',
            old_name='reduction',
            new_name='reduced_price',
        ),
    ]
