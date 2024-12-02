# Generated by Django 4.2.16 on 2024-12-02 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0004_remove_category_video'),
        ('video', '0002_alter_video_video_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='category',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='category.category'),
        ),
    ]