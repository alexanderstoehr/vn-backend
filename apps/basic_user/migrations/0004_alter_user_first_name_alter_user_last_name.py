# Generated by Django 4.2.16 on 2024-12-11 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_user', '0003_alter_user_first_name_alter_user_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, default='', max_length=150),
        ),
    ]
