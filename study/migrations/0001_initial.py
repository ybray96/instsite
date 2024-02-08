# Generated by Django 4.2.7 on 2023-12-26 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Achievements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('title_ru', models.CharField(max_length=200, null=True, verbose_name='Название')),
                ('title_en', models.CharField(max_length=200, null=True, verbose_name='Название')),
                ('title_kk', models.CharField(max_length=200, null=True, verbose_name='Название')),
                ('image', models.ImageField(default=None, upload_to='photos/%Y/%m/%d/', verbose_name='Картинка')),
                ('description', models.CharField(max_length=100, verbose_name='Достижение')),
                ('description_ru', models.CharField(max_length=100, null=True, verbose_name='Достижение')),
                ('description_en', models.CharField(max_length=100, null=True, verbose_name='Достижение')),
                ('description_kk', models.CharField(max_length=100, null=True, verbose_name='Достижение')),
            ],
            options={
                'verbose_name': 'Наша достижения',
                'verbose_name_plural': 'Наши достижения',
            },
        ),
        migrations.CreateModel(
            name='AppliedResearch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовка')),
                ('title_ru', models.CharField(max_length=200, null=True, verbose_name='Заголовка')),
                ('title_en', models.CharField(max_length=200, null=True, verbose_name='Заголовка')),
                ('title_kk', models.CharField(max_length=200, null=True, verbose_name='Заголовка')),
                ('target', models.CharField(max_length=200, verbose_name='Цель')),
                ('target_ru', models.CharField(max_length=200, null=True, verbose_name='Цель')),
                ('target_en', models.CharField(max_length=200, null=True, verbose_name='Цель')),
                ('target_kk', models.CharField(max_length=200, null=True, verbose_name='Цель')),
                ('tasks', models.TextField(verbose_name='Задачи')),
                ('tasks_ru', models.TextField(null=True, verbose_name='Задачи')),
                ('tasks_en', models.TextField(null=True, verbose_name='Задачи')),
                ('tasks_kk', models.TextField(null=True, verbose_name='Задачи')),
                ('implementation_period', models.CharField(max_length=10, verbose_name='Срок реализации')),
            ],
            options={
                'verbose_name': 'Прикладная исследования',
                'verbose_name_plural': 'Прикладные исследования',
            },
        ),
        migrations.CreateModel(
            name='Charter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовка')),
                ('title_ru', models.CharField(max_length=200, null=True, verbose_name='Заголовка')),
                ('title_en', models.CharField(max_length=200, null=True, verbose_name='Заголовка')),
                ('title_kk', models.CharField(max_length=200, null=True, verbose_name='Заголовка')),
                ('full_text', models.TextField(verbose_name='Статья')),
                ('full_text_ru', models.TextField(null=True, verbose_name='Статья')),
                ('full_text_en', models.TextField(null=True, verbose_name='Статья')),
                ('full_text_kk', models.TextField(null=True, verbose_name='Статья')),
                ('file', models.FileField(blank=True, default=None, null=True, upload_to='files/', verbose_name='Файл')),
            ],
            options={
                'verbose_name': 'Устав',
                'verbose_name_plural': 'Уставы',
            },
        ),
        migrations.CreateModel(
            name='ExpertOpinion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовка')),
                ('title_ru', models.CharField(max_length=200, null=True, verbose_name='Заголовка')),
                ('title_en', models.CharField(max_length=200, null=True, verbose_name='Заголовка')),
                ('title_kk', models.CharField(max_length=200, null=True, verbose_name='Заголовка')),
                ('description', models.TextField(verbose_name='Подробнее')),
                ('description_ru', models.TextField(null=True, verbose_name='Подробнее')),
                ('description_en', models.TextField(null=True, verbose_name='Подробнее')),
                ('description_kk', models.TextField(null=True, verbose_name='Подробнее')),
                ('date', models.DateTimeField(verbose_name='Дата публикации')),
                ('logo', models.ImageField(default=None, upload_to='photos/%Y/%m/%d/', verbose_name='Логотип')),
            ],
            options={
                'verbose_name': 'Экспертное мнение',
                'verbose_name_plural': 'Экспертные мнении',
            },
        ),
        migrations.CreateModel(
            name='InstituteStructure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовка')),
                ('title_ru', models.CharField(max_length=200, null=True, verbose_name='Заголовка')),
                ('title_en', models.CharField(max_length=200, null=True, verbose_name='Заголовка')),
                ('title_kk', models.CharField(max_length=200, null=True, verbose_name='Заголовка')),
                ('full_text', models.TextField(verbose_name='Текст')),
                ('full_text_ru', models.TextField(null=True, verbose_name='Текст')),
                ('full_text_en', models.TextField(null=True, verbose_name='Текст')),
                ('full_text_kk', models.TextField(null=True, verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Структура института',
                'verbose_name_plural': 'Структуры института',
            },
        ),
        migrations.CreateModel(
            name='MakeAnAppointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Имя')),
                ('telephone', models.CharField(max_length=200, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('date', models.DateTimeField(blank=True, verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовка')),
                ('title_ru', models.CharField(max_length=200, null=True, verbose_name='Заголовка')),
                ('title_en', models.CharField(max_length=200, null=True, verbose_name='Заголовка')),
                ('title_kk', models.CharField(max_length=200, null=True, verbose_name='Заголовка')),
                ('anons_text', models.CharField(max_length=150, verbose_name='Анонс')),
                ('anons_text_ru', models.CharField(max_length=150, null=True, verbose_name='Анонс')),
                ('anons_text_en', models.CharField(max_length=150, null=True, verbose_name='Анонс')),
                ('anons_text_kk', models.CharField(max_length=150, null=True, verbose_name='Анонс')),
                ('full_text', models.TextField(verbose_name='Статья')),
                ('full_text_ru', models.TextField(null=True, verbose_name='Статья')),
                ('full_text_en', models.TextField(null=True, verbose_name='Статья')),
                ('full_text_kk', models.TextField(null=True, verbose_name='Статья')),
                ('date', models.CharField(max_length=15, verbose_name='Дата публикации')),
                ('image', models.ImageField(default=None, upload_to='photos/%Y/%m/%d/', verbose_name='Картинка')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.CreateModel(
            name='Recomendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=200, verbose_name='Названия файла')),
                ('file_name_ru', models.CharField(max_length=200, null=True, verbose_name='Названия файла')),
                ('file_name_en', models.CharField(max_length=200, null=True, verbose_name='Названия файла')),
                ('file_name_kk', models.CharField(max_length=200, null=True, verbose_name='Названия файла')),
                ('file', models.FileField(blank=True, default=None, null=True, upload_to='files/', verbose_name='Файл')),
            ],
            options={
                'verbose_name': 'Рекомендация',
                'verbose_name_plural': 'Рекомендации',
            },
        ),
        migrations.CreateModel(
            name='ScienceLibrary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='')),
                ('title_ru', models.CharField(max_length=200, null=True, verbose_name='Название')),
                ('title_en', models.CharField(max_length=200, null=True, verbose_name='Название')),
                ('title_kk', models.CharField(max_length=200, null=True, verbose_name='Название')),
                ('image', models.ImageField(default=None, upload_to='photos/%Y/%m/%d/', verbose_name='Картинка')),
                ('minidescription', models.CharField(max_length=100, verbose_name='дата/город/автор')),
                ('minidescription_ru', models.CharField(max_length=100, null=True, verbose_name='дата/город/автор')),
                ('minidescription_en', models.CharField(max_length=100, null=True, verbose_name='дата/город/автор')),
                ('minidescription_kk', models.CharField(max_length=100, null=True, verbose_name='дата/город/автор')),
                ('file', models.FileField(blank=True, default=None, null=True, upload_to='files/', verbose_name='Файл')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Научная библиотека',
            },
        ),
        migrations.CreateModel(
            name='Scientists',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Заголовка')),
                ('name_ru', models.CharField(max_length=200, null=True, verbose_name='Заголовка')),
                ('name_en', models.CharField(max_length=200, null=True, verbose_name='Заголовка')),
                ('name_kk', models.CharField(max_length=200, null=True, verbose_name='Заголовка')),
                ('degree_of_education', models.CharField(max_length=200, verbose_name='Степень образования')),
                ('degree_of_education_ru', models.CharField(max_length=200, null=True, verbose_name='Степень образования')),
                ('degree_of_education_en', models.CharField(max_length=200, null=True, verbose_name='Степень образования')),
                ('degree_of_education_kk', models.CharField(max_length=200, null=True, verbose_name='Степень образования')),
                ('year_of_education', models.CharField(max_length=100, verbose_name='Год образования')),
                ('year_of_education_ru', models.CharField(max_length=100, null=True, verbose_name='Год образования')),
                ('year_of_education_en', models.CharField(max_length=100, null=True, verbose_name='Год образования')),
                ('year_of_education_kk', models.CharField(max_length=100, null=True, verbose_name='Год образования')),
                ('scientific_topics', models.CharField(max_length=200, verbose_name='Научные темы')),
                ('scientific_topics_ru', models.CharField(max_length=200, null=True, verbose_name='Научные темы')),
                ('scientific_topics_en', models.CharField(max_length=200, null=True, verbose_name='Научные темы')),
                ('scientific_topics_kk', models.CharField(max_length=200, null=True, verbose_name='Научные темы')),
            ],
            options={
                'verbose_name': 'Ученый',
                'verbose_name_plural': 'Ученые',
            },
        ),
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовка')),
                ('title_ru', models.CharField(max_length=200, null=True, verbose_name='Заголовка')),
                ('title_en', models.CharField(max_length=200, null=True, verbose_name='Заголовка')),
                ('title_kk', models.CharField(max_length=200, null=True, verbose_name='Заголовка')),
                ('count', models.IntegerField(verbose_name='Количество')),
            ],
            options={
                'verbose_name': 'Статистика',
                'verbose_name_plural': 'Статистики',
            },
        ),
    ]