# Generated by Django 2.2.3 on 2019-12-28 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20191227_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='contact_subtitle',
            field=models.CharField(default='Get in contact', max_length=50),
        ),
        migrations.AddField(
            model_name='homepage',
            name='contact_title',
            field=models.CharField(default='Contact', max_length=50),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='client_organisationName',
            field=models.CharField(default='My Company', max_length=50, null=True),
        ),
    ]