# Generated by Django 5.0.2 on 2024-02-27 07:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0020_alter_news_full_text_alter_news_full_text_en_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Год')),
            ],
            options={
                'verbose_name': 'Современная история категорий',
                'verbose_name_plural': 'Современная история категорий',
            },
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Заголовка')),
                ('name_ru', models.CharField(max_length=200, null=True, verbose_name='Заголовка')),
                ('name_en', models.CharField(max_length=200, null=True, verbose_name='Заголовка')),
                ('name_kk', models.CharField(max_length=200, null=True, verbose_name='Заголовка')),
                ('full_text', models.TextField(verbose_name='Статья')),
                ('full_text_ru', models.TextField(null=True, verbose_name='Статья')),
                ('full_text_en', models.TextField(null=True, verbose_name='Статья')),
                ('full_text_kk', models.TextField(null=True, verbose_name='Статья')),
                ('date', models.CharField(max_length=15, verbose_name='Дата публикации')),
                ('image', models.ImageField(default=None, upload_to='photos/%Y/%m/%d/', verbose_name='Картинка')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='History', to='study.categoryhistory')),
            ],
            options={
                'verbose_name': 'Современная история',
                'verbose_name_plural': 'Современная история',
            },
        ),
    ]