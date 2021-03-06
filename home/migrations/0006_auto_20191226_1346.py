# Generated by Django 2.2.3 on 2019-12-26 13:46

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('home', '0005_auto_20191224_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='blurb2_header_1',
            field=models.CharField(default='My Second Blurb', max_length=50),
        ),
        migrations.AddField(
            model_name='homepage',
            name='blurb2_header_2',
            field=models.CharField(default='My Second Blurb 2', max_length=50),
        ),
        migrations.AddField(
            model_name='homepage',
            name='blurb2_text',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='description',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.CreateModel(
            name='carouselOrderable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='carouselOrderable', to='home.HomePage')),
            ],
            options={
                'verbose_name': 'carousel item',
                'verbose_name_plural': 'carousel items',
            },
        ),
    ]
