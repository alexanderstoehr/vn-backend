# Generated by Django 4.2.16 on 2024-12-02 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0005_alter_userprofile_is_following'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='is_following',
            field=models.ManyToManyField(blank=True, related_name='followed_by', to='user_profile.userprofile'),
        ),
    ]
