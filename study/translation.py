from modeltranslation.translator import register, TranslationOptions
from .models import *



@register(MainSlider)
class MainSliderTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'anons_text', 'full_text')

@register(ScientistsSovet)
class ScientistsSovetTranslationOptions(TranslationOptions):
    fields = ('name', 'title_job', 'orcid')

@register(FoundationStudy)
class FoundationStudyTranslationOptions(TranslationOptions):
    fields = ('title', 'anons_text', 'full_text')

@register(Statistics)
class StatisticsTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Charter)
class ChartersTranslationOptions(TranslationOptions):
    fields = ('title', 'full_text')


@register(InstituteStructure)
class InstitutionStructureTranslationOptions(TranslationOptions):
    fields = ('title', 'full_text')


@register(Scientists)
class ScientistsTranslationOptions(TranslationOptions):
    fields = ('name', 'degree_of_education', 'year_of_education', 'scientific_topics')


@register(AppliedResearch)
class AppliedResearchTranslationOptions(TranslationOptions):
    fields = ('title', 'target', 'tasks')


@register(Recomendation)
class RecomendationTranslationOptions(TranslationOptions):
    fields = ('file_name',)


@register(ExpertOpinion)
class ExpertOpinionTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(ScienceLibrary)
class ScienceLibraryTranslationOptions(TranslationOptions):
    fields = ('title', 'minidescription')


@register(Achievements)
class AchievementsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(History)
class HistoryTranslationOptions(TranslationOptions):
    fields = ('name', 'full_text')

