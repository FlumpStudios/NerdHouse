# Generated by Django 2.2.3 on 2019-12-27 10:04

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20191226_1433'),
    ]

    operations = [
        migrations.CreateModel(
            name='enumeratedList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('text', wagtail.core.fields.RichTextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='homepage',
            name='enumerated_list_header',
            field=models.CharField(default='My enumerated list', max_length=50),
        ),
        migrations.CreateModel(
            name='enumeratedListOrderable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('enumeratedList', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='home.enumeratedList')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='enumeratedListOrderable', to='home.HomePage')),
            ],
            options={
                'verbose_name': 'Enumerated List item',
                'verbose_name_plural': 'Enumerated List items',
            },
        ),
    ]
