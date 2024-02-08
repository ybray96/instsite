# Generated by Django 4.2.8 on 2024-01-14 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0004_mainslider'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mainslider',
            options={'verbose_name': 'Слайд', 'verbose_name_plural': 'Слайды'},
        ),
        migrations.AddField(
            model_name='scientists',
            name='image',
            field=models.ImageField(default=None, upload_to='photos/%Y/%m/%d/', verbose_name='Фото'),
        ),
    ]
