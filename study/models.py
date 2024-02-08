from django.db import models
from datetime import datetime
from django.core.validators import RegexValidator
from ckeditor.fields import RichTextField
class Main(models.Model):
    image = models.ImageField("Картинка", upload_to="photos/%Y/%m/%d/", default=None)

    def __str__(self):
        return "Баннер"
    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннер"

class MainSlider(models.Model):
    title = models.CharField("Название", max_length=200)
    image = models.ImageField("Картинка", upload_to="photos/%Y/%m/%d/", default=None)
    date = models.CharField(
            max_length=10,
            blank=True,
            null=True,
            validators=[
                RegexValidator(
                    regex=r'^\d{2}\.\d{2}\.\d{4}$',
                    message='Дата должна быть в формате DD.MM.YYYY',
                ),
            ],
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Слайд"
        verbose_name_plural = "Слайды"


class News(models.Model):
    title = models.CharField("Заголовка", max_length=200)
    anons_text = models.CharField("Анонс", max_length=150)
    full_text = models.TextField("Статья")
    date = models.CharField("Дата публикации", max_length=15)
    image = models.ImageField("Картинка", upload_to="photos/%Y/%m/%d/", default=None)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


class Statistics(models.Model):
    title = models.CharField("Заголовка", max_length=200)
    count = models.IntegerField("Количество")

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Статистика"
        verbose_name_plural = "Статистики"


class Charter(models.Model):
    title = models.CharField("Заголовка", max_length=200)
    full_text = models.TextField("Статья")
    file = models.FileField(
        "Файл", upload_to="files/", null=True, default=None, blank=True
    )

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Устав"
        verbose_name_plural = "Уставы"


class InstituteStructure(models.Model):
    title = models.CharField("Заголовка", max_length=200)
    full_text = models.TextField("Текст")

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Структура института"
        verbose_name_plural = "Структуры института"


class Scientists(models.Model):
    name = models.CharField("Заголовка", max_length=200)
    degree_of_education = models.CharField("Степень образования", max_length=200)
    year_of_education = models.CharField("Год образования", max_length=100)
    scientific_topics = models.CharField("Научные темы", max_length=200)
    image = models.ImageField("Фото", upload_to="photos/%Y/%m/%d/", default='default_image.jpg')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Ученый"
        verbose_name_plural = "Ученые"


class ScientistsSovet(models.Model):
    name = models.CharField("ФИО", max_length=200)
    title_job = models.CharField("Должность", max_length=200)
    orcid = models.CharField("ORCID", blank=True, null=True, max_length=200)
    image = models.ImageField("Фото", upload_to="photos/%Y/%m/%d/", default='default_image.jpg')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Ученый совет"
        verbose_name_plural = "Ученый совет"

class AppliedResearch(models.Model):
    title = models.CharField("Заголовка", max_length=200)
    target = models.CharField("Цель", max_length=200)
    tasks = models.TextField("Задачи")
    implementation_period = models.CharField("Срок реализации", max_length=10)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Прикладная исследования"
        verbose_name_plural = "Прикладные исследования"


class Recomendation(models.Model):
    file_name = models.CharField("Названия файла", max_length=200)
    file = models.FileField(
        "Файл", upload_to="files/", null=True, default=None, blank=True
    )

    def __str__(self):
        return self.file_name
    class Meta:
        verbose_name = "Рекомендация"
        verbose_name_plural = "Рекомендации"


class ExpertOpinion(models.Model):
    title = models.CharField("Заголовка", max_length=200)
    description = models.TextField("Подробнее")
    date = models.DateTimeField("Дата публикации")
    logo = models.ImageField("Логотип", upload_to="photos/%Y/%m/%d/", default=None)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Экспертное мнение"
        verbose_name_plural = "Экспертные мнении"


class ScienceLibrary(models.Model):
    title = models.CharField("Название", max_length=200)
    image = models.ImageField("Картинка", upload_to="photos/%Y/%m/%d/", default=None)
    minidescription = models.CharField("дата/город/автор", max_length=100)
    file = models.FileField(
        "Файл", upload_to="files/", null=True, default=None, blank=True
    )

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Научная библиотека"


class Achievements(models.Model):
    title = models.CharField("Название", max_length=200)
    image = models.ImageField("Картинка", upload_to="photos/%Y/%m/%d/", default=None)
    description = models.TextField("Достижение")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Наша достижения"
        verbose_name_plural = "Наши достижения"


class MakeAnAppointment(models.Model):
    name = models.CharField("Имя", max_length=200)
    telephone = models.CharField("Номер телефона", max_length=200)
    email = models.EmailField("Почта")
    date = models.DateTimeField("Дата", blank=True)
    #
    # def save(self, *args, **kwargs):
    #     self.date = datetime.strptime(self.date, "%d.%m.%Y").strftime("%Y-%m-%d")
    #     super().save(*args, **kwargs)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"


class FoundationStudy(models.Model):
    title = models.CharField("Заголовка", max_length=200)
    anons_text = models.CharField("Анонс", max_length=150)
    full_text = models.TextField("Статья")
    date = models.CharField("Дата публикации", max_length=15)
    image = models.ImageField("Картинка", upload_to="photos/%Y/%m/%d/", default=None)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Исследование"
        verbose_name_plural = "Исследования"


