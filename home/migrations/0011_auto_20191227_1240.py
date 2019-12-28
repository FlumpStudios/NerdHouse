# Generated by Django 2.2.3 on 2019-12-27 12:40

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('home', '0010_auto_20191227_1123'),
    ]

    operations = [
        migrations.CreateModel(
            name='testimonialItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50)),
                ('testimonial', wagtail.core.fields.RichTextField(blank=True)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='blurb_header_1',
            new_name='blurb_header',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='blurb2_buttonText',
            new_name='second_blurb_buttonText',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='blurb2_header_1',
            new_name='second_blurb_header',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='blurb2_header_2',
            new_name='second_blurb_subheader',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='blurb2_text',
            new_name='second_blurb_text',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='blurb2_link',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='blurb_header_2',
        ),
        migrations.AddField(
            model_name='homepage',
            name='blurb_buttonText',
            field=models.CharField(default='Find out more', max_length=50),
        ),
        migrations.AddField(
            model_name='homepage',
            name='blurb_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='blurb_subheader',
            field=models.CharField(default='this is a blurb ', max_length=50),
        ),
        migrations.AddField(
            model_name='homepage',
            name='second_blurb_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='testimonials_header',
            field=models.CharField(default='Testimonials', max_length=50),
        ),
        migrations.AlterField(
            model_name='iconitem',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='testimonialOrderable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='testimonialOrderable', to='home.HomePage')),
                ('testimonialItem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='home.testimonialItem')),
            ],
            options={
                'verbose_name': 'Testimonial List item',
                'verbose_name_plural': 'Testimonial List items',
            },
        ),
    ]
