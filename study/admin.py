from django.contrib import admin
from .models import *
from django import forms
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from modeltranslation.admin import TranslationAdmin
from django.utils.html import format_html


# admin.site.index_title = "Институт"
admin.site.site_header = "Администрирование сайта"
admin.site.site_title = "Институт истории государства"

class MainAdmin(admin.ModelAdmin):
   list_display = ('id',)
   def has_add_permission(self, request):
      if Main.objects.exists():
         return False
      return True

class MainSliderAdminForm(forms.ModelForm):
    class Meta:
        model = Recomendation
        fields = '__all__'


class MainSliderAdmin(TranslationAdmin):
    list_display = ('title',)
    form = MainSliderAdminForm

class NewsAdminForm(forms.ModelForm):
    anons_text_ru = forms.CharField(label='Анонс [ru]', widget=CKEditorUploadingWidget())
    anons_text_en = forms.CharField(label='Анонс [en]', required=False, widget=CKEditorUploadingWidget())
    anons_text_kk = forms.CharField(label='Анонс [kk]', required=False, widget=CKEditorUploadingWidget())
    full_text_ru = forms.CharField(label='Статья [ru]', widget=CKEditorUploadingWidget())
    full_text_en = forms.CharField(label='Статья [en]', required=False, widget=CKEditorUploadingWidget())
    full_text_kk = forms.CharField(label='Статья [kk]', required=False, widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


class NewsAdmin(TranslationAdmin):
    list_display = ('title', 'anons_text', 'date')
    form = NewsAdminForm

class FoundationStudyAdminForm(forms.ModelForm):
    anons_text_ru = forms.CharField(label='Анонс [ru]', widget=CKEditorUploadingWidget())
    anons_text_en = forms.CharField(label='Анонс [en]', required=False, widget=CKEditorUploadingWidget())
    anons_text_kk = forms.CharField(label='Анонс [kk]', required=False, widget=CKEditorUploadingWidget())
    full_text_ru = forms.CharField(label='Статья [ru]', widget=CKEditorUploadingWidget())
    full_text_en = forms.CharField(label='Статья [en]', required=False, widget=CKEditorUploadingWidget())
    full_text_kk = forms.CharField(label='Статья [kk]', required=False, widget=CKEditorUploadingWidget())

    class Meta:
        model = FoundationStudy
        fields = '__all__'


class FoundationStudyAdmin(TranslationAdmin):
    list_display = ('title', 'anons_text', 'date')
    form = FoundationStudyAdminForm


class StatisticsAdmin(TranslationAdmin):
    list_display = ('title',)


class CharterAdminForm(forms.ModelForm):
    full_text_ru = forms.CharField(label='Статья [ru]', widget=CKEditorUploadingWidget())
    full_text_en = forms.CharField(label='Статья [en]', required=False, widget=CKEditorUploadingWidget())
    full_text_kk = forms.CharField(label='Статья [kk]', required=False, widget=CKEditorUploadingWidget())

    class Meta:
        model = Charter
        fields = '__all__'


class CharterAdmin(TranslationAdmin):
    list_display = ('title',)
    form = CharterAdminForm


class InstituteStructureAdminForm(forms.ModelForm):
    full_text_ru = forms.CharField(label='Текст [ru]', widget=CKEditorUploadingWidget())
    full_text_en = forms.CharField(label='Текст [en]', required=False, widget=CKEditorUploadingWidget())
    full_text_kk = forms.CharField(label='Текст [kk]', required=False, widget=CKEditorUploadingWidget())

    class Meta:
        model = InstituteStructure
        fields = '__all__'


class InstituteStructureAdmin(TranslationAdmin):
    list_display = ('title',)
    form = InstituteStructureAdminForm


class ScientistsAdminForm(forms.ModelForm):
    class Meta:
        model = Scientists
        fields = '__all__'


class ScientistsAdmin(TranslationAdmin):
    list_display = ('name', 'degree_of_education')
    form = ScientistsAdminForm


class ScientistsSovetAdminForm(forms.ModelForm):
    class Meta:
        model = ScientistsSovet
        fields = '__all__'


class ScientistsSovetAdmin(TranslationAdmin):
    list_display = ('name', 'title_job')
    form = ScientistsSovetAdminForm

class AppliedResearchAdminForm(forms.ModelForm):
    tasks_ru = forms.CharField(label='Задачи [ru]', widget=CKEditorUploadingWidget())
    tasks_en = forms.CharField(label='Задачи [en]', required=False, widget=CKEditorUploadingWidget())
    tasks_kk = forms.CharField(label='Задачи [kk]', required=False, widget=CKEditorUploadingWidget())

    class Meta:
        model = AppliedResearch
        fields = '__all__'


class AppliedResearchAdmin(TranslationAdmin):
    list_display = ('title',)
    form = AppliedResearchAdminForm


class RecomendationAdminForm(forms.ModelForm):
    class Meta:
        model = Recomendation
        fields = '__all__'


class RecomendationAdmin(TranslationAdmin):
    list_display = ('file_name',)
    form = RecomendationAdminForm


class ExpertOpinionAdminForm(forms.ModelForm):
    description_ru = forms.CharField(label='Подробнее [ru]', widget=CKEditorUploadingWidget())
    description_en = forms.CharField(label='Подробнее [en]', required=False, widget=CKEditorUploadingWidget())
    description_kk = forms.CharField(label='Подробнее [kk]', required=False, widget=CKEditorUploadingWidget())

    class Meta:
        model = ExpertOpinion
        fields = '__all__'


class ExpertOpinionAdmin(TranslationAdmin):
    list_display = ('title', 'link')
    form = ExpertOpinionAdminForm


class ScienceLibraryAdminForm(forms.ModelForm):
    class Meta:
        model = ScienceLibrary
        fields = '__all__'


class ScienceLibraryAdmin(TranslationAdmin):
    list_display = ('title',)
    form = ScienceLibraryAdminForm


class AchievementsAdminForm(forms.ModelForm):
    class Meta:
        model = Achievements
        fields = '__all__'


class AchievementsAdmin(TranslationAdmin):
    list_display = ('title',)
    form = AchievementsAdminForm


admin.site.register(Main, MainAdmin)
admin.site.register(MainSlider, MainSliderAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(FoundationStudy, FoundationStudyAdmin)
admin.site.register(Statistics, StatisticsAdmin)
admin.site.register(Charter, CharterAdmin)
admin.site.register(ScientistsSovet, ScientistsSovetAdmin)
admin.site.register(InstituteStructure, InstituteStructureAdmin)
admin.site.register(Scientists, ScientistsAdmin)
admin.site.register(AppliedResearch, AppliedResearchAdmin)
admin.site.register(Recomendation, RecomendationAdmin)
admin.site.register(ExpertOpinion, ExpertOpinionAdmin)
admin.site.register(ScienceLibrary, ScienceLibraryAdmin)
admin.site.register(Achievements, AchievementsAdmin)
admin.site.register(MakeAnAppointment)
