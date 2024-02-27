from django.forms import model_to_dict
from django.shortcuts import render

from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets, generics
from .serializers import GroupSerializer, UserSerializer
from .models import News
from .serializers import NewsSerializer
from rest_framework.views import APIView
from django.db.models import Q
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework import serializers
from rest_framework.response import Response
from django.db.models import Q
from .models import News, Statistics, Charter, InstituteStructure, Scientists, ScientistsSovet, AppliedResearch, Recomendation, ExpertOpinion, ScienceLibrary, Achievements, MakeAnAppointment, FoundationStudy
from .serializers import NewsSerializer, StatisticsSerializer, CharterSerializer, InstituteStructureSerializer, ScientistsSerializer, ScientistsSovetSerializer, AppliedResearchSerializer, RecomendationSerializer, ExpertOpinionSerializer, ScienceLibrarySerializer, AchievementsSerializer, MakeAnAppointmentSerializer, FoundationStudySerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class MainApiView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        items = Main.objects.all()
        serializer = MainSerializer(items, many=True)
        return Response({"data": serializer.data})

class MainSliderApiView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        items = MainSlider.objects.all()
        serializer = MainSliderSerializer(items, many=True)
        return Response({"data": serializer.data})


# class NewsApiView(APIView):
#     permission_classes = [AllowAny]
#     def get(self, request):
#         items = News.objects.all().values()
#         return Response({'data': list(items)})


class NewsListView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


# class NewsListCreateView(generics.ListCreateAPIView):
#     queryset = News.objects.all()
#     serializer_class = NewsSerializer


class NewsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class FoundationStudyApiView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        items = FoundationStudy.objects.all()
        serializer = FoundationStudySerializer(items, many=True)
        return Response({"data": serializer.data})


class FoundationStudyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FoundationStudy.objects.all()
    serializer_class = FoundationStudySerializer

class StatisticsApiView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        items = Statistics.objects.all()
        serializer = StatisticsSerializer(items, many=True)
        return Response({"data": serializer.data})


class CharterApiView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        items = Charter.objects.all()
        serializer = CharterSerializer(items, many=True)
        return Response({"data": serializer.data})


class ScientistsSovetApiView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        items = ScientistsSovet.objects.all()
        serializer = ScientistsSovetSerializer(items, many=True)
        return Response({"data": serializer.data})
class InstituteStructureApiView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        items = InstituteStructure.objects.all()
        serializer = InstituteStructureSerializer(items, many=True)
        return Response({"data": serializer.data})


class ScientistsApiView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        items = Scientists.objects.all()
        serializer = ScientistsSerializer(items, many=True)
        return Response({"data": serializer.data})

class AppliedResearchApiView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        items = AppliedResearch.objects.all()
        serializer = AppliedResearchSerializer(items, many=True)
        return Response({"data": serializer.data})

class RecomendationApiView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        items = Recomendation.objects.all()
        serializer = RecomendationSerializer(items, many=True)
        return Response({"data": serializer.data})


class ExpertOpinionApiView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        items = ExpertOpinion.objects.all()
        serializer = ExpertOpinionSerializer(items, many=True)
        return Response({"data": serializer.data})

class ScienceLibraryApiView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        items = ScienceLibrary.objects.all()
        serializer = ScienceLibrarySerializer(items, many=True)
        return Response({"data": serializer.data})


class AchievementsApiView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        items = Achievements.objects.all()
        serializer = AchievementsSerializer(items, many=True)
        return Response({"data": serializer.data})


class MakeAnAppointmentCreateView(generics.ListCreateAPIView):
    permission_classes = [AllowAny]

    queryset = MakeAnAppointment.objects.all()
    serializer_class = MakeAnAppointmentSerializer

class HistoryApiView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        items = History.objects.all()
        serializer = HistorySerializer(items, many=True)
        return Response({"data": serializer.data})

class CategoryHistoryApiView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        items = CategoryHistory.objects.all()
        serializer = CategoryHistorySerializer(items, many=True)
        return Response({"data": serializer.data})

class GlobalSearchAPIView(generics.ListAPIView):
    def get_serializer_class(self):
        model = self.request.query_params.get('model', None)
        if model == 'news':
            return NewsSerializer
        elif model == 'statistics':
            return StatisticsSerializer
        elif model == 'charter':
            return CharterSerializer
        elif model == 'institute_structure':
            return InstituteStructureSerializer
        elif model == 'scientists':
            return ScientistsSerializer
        elif model == 'scientists_sovet':
            return ScientistsSovetSerializer
        elif model == 'applied_research':
            return AppliedResearchSerializer
        elif model == 'recomendation':
            return RecomendationSerializer
        elif model == 'expert_opinion':
            return ExpertOpinionSerializer
        elif model == 'science_library':
            return ScienceLibrarySerializer
        elif model == 'achievements':
            return AchievementsSerializer
        elif model == 'make_an_appointment':
            return MakeAnAppointmentSerializer
        elif model == 'foundation_study':
            return FoundationStudySerializer
        return serializers.Serializer  # Возвращаем значение по умолчанию

    def get_queryset(self):
        query = self.request.query_params.get('query', '')
        model = self.request.query_params.get('model', None)
        if model == 'news':
            return News.objects.filter(
                Q(title__icontains=query) | Q(anons_text__icontains=query) | Q(full_text__icontains=query) | Q(date__icontains=query)
            )
        elif model == 'statistics':
            return Statistics.objects.filter(
                Q(title__icontains=query) | Q(count__icontains=query)
            )
        elif model == 'charter':
            return Charter.objects.filter(
                Q(title__icontains=query) | Q(full_text__icontains=query)
            )
        elif model == 'institute_structure':
            return InstituteStructure.objects.filter(
                Q(title__icontains=query) | Q(full_text__icontains=query)
            )
        elif model == 'scientists':
            return Scientists.objects.filter(
                Q(name__icontains=query) | Q(degree_of_education__icontains=query) | Q(year_of_education__icontains=query) | Q(scientific_topics__icontains=query)
            )
        elif model == 'scientists_sovet':
            return ScientistsSovet.objects.filter(
                Q(name__icontains=query) | Q(title_job__icontains=query) | Q(orcid__icontains=query)
            )
        elif model == 'applied_research':
            return AppliedResearch.objects.filter(
                Q(title__icontains=query) | Q(target__icontains=query) | Q(tasks__icontains=query) | Q(implementation_period__icontains=query)
            )
        elif model == 'recomendation':
            return Recomendation.objects.filter(
                Q(file_name__icontains=query)
            )
        elif model == 'expert_opinion':
            return ExpertOpinion.objects.filter(
                Q(title__icontains=query) | Q(description__icontains=query) | Q(date__icontains=query)
            )
        elif model == 'science_library':
            return ScienceLibrary.objects.filter(
                Q(title__icontains=query) | Q(minidescription__icontains=query)
            )
        elif model == 'achievements':
            return Achievements.objects.filter(
                Q(title__icontains=query) | Q(description__icontains=query)
            )
        elif model == 'make_an_appointment':
            return MakeAnAppointment.objects.filter(
                Q(name__icontains=query) | Q(telephone__icontains=query) | Q(email__icontains=query) | Q(date__icontains=query)
            )
        elif model == 'foundation_study':
            return FoundationStudy.objects.filter(
                Q(title__icontains=query) | Q(anons_text__icontains=query) | Q(full_text__icontains=query) | Q(date__icontains=query)
            )
        return None

