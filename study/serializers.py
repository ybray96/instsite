from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class MainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Main
        fields = "__all__"

class MainSliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainSlider
        fields = "__all__"

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"

class ScientistsSovetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScientistsSovet
        fields = "__all__"

class FoundationStudySerializer(serializers.ModelSerializer):
    class Meta:
        model = FoundationStudy
        fields = "__all__"


class StatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistics
        fields = "__all__"


class CharterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Charter
        fields = "__all__"


# class InstituteStructureSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = InstituteStructure
#         fields = ['title', 'full_text']

class InstituteStructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstituteStructure
        fields = "__all__"

class ScientistsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scientists
        fields = "__all__"


class AppliedResearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppliedResearch
        fields = "__all__"


class RecomendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recomendation
        fields = "__all__"


class ExpertOpinionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpertOpinion
        fields = "__all__"


# class ScienceLibrarySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ScienceLibrary
#         fields = ['title', 'image', 'minidescription', 'file']
class ScienceLibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = ScienceLibrary
        fields = "__all__"


class AchievementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievements
        fields = "__all__"


class MakeAnAppointmentSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format="%d.%m.%Y")
    class Meta:
        model = MakeAnAppointment
        fields = '__all__'


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = "__all__"

class CategoryHistorySerializer(serializers.ModelSerializer):
    products = HistorySerializer(many=True, read_only=True)

    class Meta:
        model = CategoryHistory
        fields = "__all__"
