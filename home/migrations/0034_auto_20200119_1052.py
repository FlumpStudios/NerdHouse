# Generated by Django 2.2 on 2020-01-19 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0033_auto_20200119_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='custom_css',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='custom_html',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='custom_javacript',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]