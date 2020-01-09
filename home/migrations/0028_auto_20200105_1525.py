# Generated by Django 2.2.3 on 2020-01-05 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_auto_20200105_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='client_email',
            field=models.CharField(default='joe@bloggs.com', max_length=50),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='client_organisationName',
            field=models.CharField(blank=True, default='My Company', max_length=50),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='second_blurb_link',
            field=models.URLField(blank=True, default='#'),
        ),
    ]