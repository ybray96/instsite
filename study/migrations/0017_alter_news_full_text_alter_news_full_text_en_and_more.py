# Generated by Django 4.2.8 on 2024-01-23 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0016_alter_news_full_text_alter_news_full_text_en_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='full_text',
            field=models.TextField(verbose_name='Статья'),
        ),
        migrations.AlterField(
            model_name='news',
            name='full_text_en',
            field=models.TextField(null=True, verbose_name='Статья'),
        ),
        migrations.AlterField(
            model_name='news',
            name='full_text_kk',
            field=models.TextField(null=True, verbose_name='Статья'),
        ),
        migrations.AlterField(
            model_name='news',
            name='full_text_ru',
            field=models.TextField(null=True, verbose_name='Статья'),
        ),
    ]
