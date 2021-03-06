# Generated by Django 2.2.3 on 2020-01-06 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0028_auto_20200105_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='intro_youtube_id',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AddField(
            model_name='homepage',
            name='video_background_brightness',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=3),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='intro_continue_button_text',
            field=models.CharField(blank=True, default='Continue', max_length=50),
        ),
    ]
