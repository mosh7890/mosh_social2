# Generated by Django 2.2 on 2019-04-24 14:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', stdimage.models.StdImageField(help_text='Picture:JPG/JPEG', upload_to='posts/images', verbose_name='Image')),
                ('caption', models.CharField(default='', help_text='Caption/Description', max_length=255, verbose_name='Caption')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date/Time.', verbose_name='Created At')),
                ('author', models.ForeignKey(help_text='Uploader', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_posts', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'db_table': 'posts',
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(help_text='Comment', max_length=255, verbose_name='Comment')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date/Time.', verbose_name='Created At')),
                ('author', models.ForeignKey(help_text='Author', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_comments', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('post', models.ForeignKey(help_text='Post', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='post_comments', to='posts.Post', verbose_name='Post')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
                'db_table': 'comments',
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date/Time.', verbose_name='Created At')),
                ('author', models.ForeignKey(help_text='Author', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_likes', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('post', models.ForeignKey(help_text='Post', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='post_likes', to='posts.Post', verbose_name='Post')),
            ],
            options={
                'verbose_name': 'Like',
                'verbose_name_plural': 'Likes',
                'db_table': 'likes',
                'ordering': ('created_at',),
                'unique_together': {('author', 'post')},
            },
        ),
    ]