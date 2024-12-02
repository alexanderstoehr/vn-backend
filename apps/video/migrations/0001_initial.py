# Generated by Django 4.2.16 on 2024-12-01 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('space', '0002_space_is_public'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_title', models.CharField(max_length=100)),
                ('video_description', models.TextField(blank=True, max_length=2500, null=True)),
                ('video_host_url', models.TextField(max_length=200)),
                ('video_host_id', models.TextField(max_length=100)),
                ('video_host_thumbnail_url', models.TextField(max_length=200)),
                ('is_public', models.BooleanField(default=False)),
                ('is_shareable', models.BooleanField(default=False)),
                ('is_shareable_to_all', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('space', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='space.space')),
            ],
        ),
    ]