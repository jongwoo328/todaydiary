# Generated by Django 2.2.15 on 2020-11-25 06:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import post.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Emotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('path', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pattern',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(blank=True, max_length=100, null=True)),
                ('preview_path', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('created', models.DateField()),
                ('image', models.ImageField(blank=True, null=True, upload_to=post.models.upload_location)),
                ('sticker_image', models.ImageField(blank=True, default=None, null=True, upload_to=post.models.upload_sticker_location)),
            ],
        ),
        migrations.CreateModel(
            name='PostColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PostFont',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('path', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Sticker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=100)),
                ('emotion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stickers', to='post.Emotion')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stickers', to='post.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='SearchMusic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('artist', models.CharField(blank=True, max_length=30, null=True)),
                ('video_id', models.CharField(max_length=20)),
                ('cover', models.TextField(blank=True, null=True)),
                ('emotion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='search_musics', to='post.Emotion')),
                ('post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='post', to='post.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='search_music', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RecommendMusic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('artist', models.CharField(blank=True, max_length=30, null=True)),
                ('video_id', models.CharField(max_length=20)),
                ('cover', models.TextField(blank=True, null=True)),
                ('emotion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='musics', to='post.Emotion')),
            ],
        ),
        migrations.CreateModel(
            name='PostSticker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('width', models.CharField(max_length=20)),
                ('rotation', models.CharField(max_length=20)),
                ('y', models.CharField(max_length=20)),
                ('x', models.CharField(max_length=20)),
                ('scaleY', models.CharField(default=0, max_length=20)),
                ('scaleX', models.CharField(default=0, max_length=20)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stickers', to='post.Post')),
                ('sticker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Sticker')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='font',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.PostFont'),
        ),
        migrations.AddField(
            model_name='post',
            name='pattern',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Pattern'),
        ),
        migrations.AddField(
            model_name='post',
            name='recommend_music',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recommend_music', to='post.RecommendMusic'),
        ),
    ]
