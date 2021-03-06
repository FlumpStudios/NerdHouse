# Generated by Django 2.2.9 on 2019-12-28 22:31

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20191228_1054'),
    ]

    operations = [
        migrations.CreateModel(
            name='socialMediaItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('link', models.URLField(blank=True, null=True)),
                ('icon', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='socialMediaOrderable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='socialMediaOrderable', to='home.HomePage')),
                ('socialMediaItem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='home.socialMediaItem')),
            ],
            options={
                'verbose_name': 'Social Media item',
                'verbose_name_plural': 'Social Media items',
            },
        ),
    ]
