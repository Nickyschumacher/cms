# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-02-24 07:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('img_url', models.CharField(max_length=255, verbose_name='图片url')),
                ('tags', models.TextField(verbose_name='标识')),
                ('zhaiyao', models.CharField(max_length=255, verbose_name='摘要')),
                ('content', models.TextField(verbose_name='新闻内容')),
                ('click', models.IntegerField(verbose_name='点击量')),
                ('status', models.IntegerField(verbose_name='是否下线')),
                ('is_top', models.IntegerField(verbose_name='是否头条')),
                ('is_slide', models.IntegerField(verbose_name='是否轮播新闻')),
                ('source', models.CharField(max_length=20, verbose_name='新闻来源')),
                ('author', models.CharField(max_length=20, verbose_name='作者')),
            ],
            options={
                'verbose_name_plural': '新闻数据',
                'verbose_name': '新闻数据',
                'db_table': 't_news',
            },
        ),
        migrations.CreateModel(
            name='NewsAlbum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('thumb_path', models.CharField(max_length=255, verbose_name='缩略图url')),
                ('original_path', models.CharField(max_length=255, verbose_name='原图url')),
                ('remark', models.TextField(null=True, verbose_name='备注信息')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.News')),
            ],
            options={
                'verbose_name_plural': '新闻图片',
                'verbose_name': '新闻图片',
                'db_table': 't_news_album',
            },
        ),
        migrations.CreateModel(
            name='NewsCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('title', models.CharField(max_length=100, verbose_name='类别名称')),
                ('sort_id', models.IntegerField(verbose_name='排序权重')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.NewsCategory', verbose_name='父类别')),
            ],
            options={
                'verbose_name_plural': '新闻分类',
                'verbose_name': '新闻分类',
                'db_table': 't_news_category',
            },
        ),
        migrations.AddField(
            model_name='news',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.NewsCategory', verbose_name='所属类别'),
        ),
    ]
