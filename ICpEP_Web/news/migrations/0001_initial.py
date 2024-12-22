# Generated by Django 5.1.3 on 2024-11-17 12:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsArticle',
            fields=[
                ('article_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('publication_date', models.DateTimeField(auto_now_add=True)),
                ('view_count', models.PositiveIntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'NewsArticles',
            },
        ),
        migrations.CreateModel(
            name='ArticlePhoto',
            fields=[
                ('photo_id', models.AutoField(primary_key=True, serialize=False)),
                ('image_path', models.ImageField(blank=True, null=True, upload_to='article_photos/')),
                ('caption', models.CharField(blank=True, max_length=255, null=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='news.newsarticle')),
            ],
            options={
                'db_table': 'ArticlePhotos',
            },
        ),
        migrations.CreateModel(
            name='NewsView',
            fields=[
                ('view_id', models.AutoField(primary_key=True, serialize=False)),
                ('viewed_at', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.newsarticle')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'NewsViews',
                'unique_together': {('student', 'article')},
            },
        ),
    ]
