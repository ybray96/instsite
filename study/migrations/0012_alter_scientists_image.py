# Generated by Django 4.2.8 on 2024-01-14 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0011_alter_scientists_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scientists',
            name='image',
            field=models.ImageField(default='default_image.jpg', upload_to='photos/%Y/%m/%d/', verbose_name='Фото'),
        ),
    ]