# Generated by Django 4.2.16 on 2024-12-01 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='about_me',
            field=models.TextField(blank=True, null=True),
        ),
    ]
