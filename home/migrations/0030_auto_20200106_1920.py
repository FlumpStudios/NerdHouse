# Generated by Django 2.2.9 on 2020-01-06 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0029_auto_20200106_0754'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='intro_youtube_id',
            new_name='intro_video_id',
        ),
    ]