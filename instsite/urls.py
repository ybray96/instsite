"""inst URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from rest_framework import routers
from study import views
from study.views import *
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)
# router.register(r'News', views.NewsApiView)
# router.register(r'Statistics', views.StatisticsApiView)
# router.register(r'Charter', views.CharterApiView)
# router.register(r'institutes-structure', views.InstitutesStructureApiView)
# router.register(r'scientists', views.ScientistsApiView)
# router.register(r'AppliedResearch', views.AppliedResearchApiView)
# router.register(r'recomendations', views.RecomendationsApiView)
# router.register(r'ExpertOpinion', views.ExpertOpinionApiView)
# router.register(r'ScienceLibrary', views.ScienceLibraryApiView)
# router.register(r'Achievements', views.AchievementsApiView)
# router.register(r'MakeAnAppointment', views.MakeAnAppointmentCreateView)


urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("admin/", admin.site.urls),
    path("api/v1/main-list/", MainApiView.as_view()),
    path("api/v1/mainslider-list/", MainSliderApiView.as_view()),
    path("api/v1/news-list/", NewsListView.as_view()),
    # path('api/v1/news-list/', NewsListCreateView.as_view(), name='news-list-create'),
    path(
        "api/v1/news-list/<int:pk>/",
        NewsRetrieveUpdateDestroyView.as_view(),
        name="news-detail",
    ),
    path("api/v1/foundation-study-list/", FoundationStudyApiView.as_view()),
    path("api/v1/scientists-sovet-list/", ScientistsSovetApiView.as_view()),
    path("api/v1/foundation-study-list/<int:pk>/", FoundationStudyRetrieveUpdateDestroyView.as_view()),
    path("api/v1/statistics-list/", StatisticsApiView.as_view()),
    path("api/v1/charter-list/", CharterApiView.as_view()),
    path("api/v1/institutes-structure-list/", InstituteStructureApiView.as_view()),
    path("api/v1/scientists-list/", ScientistsApiView.as_view()),
    path("api/v1/applied-research-list/", AppliedResearchApiView.as_view()),
    path("api/v1/recomendation-list/", RecomendationApiView.as_view()),
    path("api/v1/expert-opinion-list/", ExpertOpinionApiView.as_view()),
    path("api/v1/science-library-list/", ScienceLibraryApiView.as_view()),
    path("api/v1/achievements-list/", AchievementsApiView.as_view()),
    path("api/v1/make-appointment-list/", MakeAnAppointmentCreateView.as_view()),
    path('api/v1/search/', GlobalSearchAPIView.as_view(), name='global-search'),
    path('api/v1/categories-history/', CategoryHistoryApiView.as_view(), name='categories-history'),
    path('api/v1/history/', HistoryApiView.as_view(), name='history'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += router.urls
