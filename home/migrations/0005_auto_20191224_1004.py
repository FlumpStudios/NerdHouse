# Generated by Django 2.2.3 on 2019-12-24 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20191224_1001'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='galleryorderable',
            options={'verbose_name': 'gallery item', 'verbose_name_plural': 'gallery items'},
        ),
    ]