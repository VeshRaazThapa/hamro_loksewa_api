# Generated by Django 5.1.4 on 2025-02-02 12:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0005_package_seo_card_image_package_seo_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ebook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('featured_image', models.ImageField(upload_to='ebooks/images/')),
                ('file_url', models.FileField(upload_to='ebooks/files/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='package.package')),
            ],
            options={
                'verbose_name': 'Ebook',
                'verbose_name_plural': 'Ebooks',
                'db_table': 'ebooks',
                'ordering': ['-created_at'],
            },
        ),
    ]
