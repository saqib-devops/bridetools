# Generated by Django 3.2.19 on 2023-06-20 14:05

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_auto_20230620_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='divider_logo_1',
            field=models.ImageField(blank=True, null=True, upload_to='home/divider'),
        ),
        migrations.AddField(
            model_name='site',
            name='divider_logo_2',
            field=models.ImageField(blank=True, null=True, upload_to='home/divider'),
        ),
        migrations.AddField(
            model_name='site',
            name='divider_logo_3',
            field=models.ImageField(blank=True, null=True, upload_to='home/divider'),
        ),
        migrations.AddField(
            model_name='site',
            name='divider_logo_4',
            field=models.ImageField(blank=True, null=True, upload_to='home/divider'),
        ),
        migrations.AddField(
            model_name='site',
            name='divider_short_discription_1',
            field=tinymce.models.HTMLField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='site',
            name='divider_short_discription_2',
            field=tinymce.models.HTMLField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='site',
            name='divider_short_discription_3',
            field=tinymce.models.HTMLField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='site',
            name='divider_short_discription_4',
            field=tinymce.models.HTMLField(default=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='site',
            name='divider_title_1',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='site',
            name='divider_title_2',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='site',
            name='divider_title_3',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='site',
            name='divider_title_4',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
