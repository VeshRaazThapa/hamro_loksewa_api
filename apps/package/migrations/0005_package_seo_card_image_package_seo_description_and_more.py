# Generated by Django 5.1.4 on 2025-02-02 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0004_package_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='seo_card_image',
            field=models.FileField(blank=True, null=True, upload_to='package/seo/'),
        ),
        migrations.AddField(
            model_name='package',
            name='seo_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='package',
            name='seo_title',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='package',
            name='seo_twitter_card_type',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
