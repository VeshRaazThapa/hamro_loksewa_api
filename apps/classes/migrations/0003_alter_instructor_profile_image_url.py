# Generated by Django 5.1.4 on 2025-02-02 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0002_alter_instructor_profile_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='profile_image_url',
            field=models.ImageField(upload_to='instructor/profile/'),
        ),
    ]
