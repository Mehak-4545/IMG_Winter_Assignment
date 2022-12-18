"""companyapi URL Configuration

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
from django.urls import path, include
from backend import views
from .views import *
from backend import views
from rest_framework.routers import DefaultRouter

from django.contrib import admin
from django.urls import path, include
from backend.views import RecruitmentSeasonModelViewSet, RoundModelViewSet, SectionModelViewSet, QuestionModelViewSet, CandidateModelViewSet, UserModelViewSet, EvaluatorPanelModelViewSet, CandidateRoundModelViewSet, CandidateQuestionModelViewSet
from rest_framework import routers


# Creating default router object
router = routers.DefaultRouter()


# Register Viewsets with router
router.register(r'recruitmentseason', RecruitmentSeasonModelViewSet)
router.register(r'round', RoundModelViewSet)
router.register(r'section', SectionModelViewSet)
router.register(r'question', QuestionModelViewSet)
router.register(r'candidate', CandidateModelViewSet)
router.register(r'user', UserModelViewSet)
router.register(r'evaluatorpanel', EvaluatorPanelModelViewSet)
router.register(r'candidaterounds', CandidateRoundModelViewSet)
router.register(r'candidatequestion', CandidateQuestionModelViewSet)


urlpatterns = [

    path('admin/', admin.site.urls),
    path("home/", home_page),
    path("profile/", profile_page),
    # path("dashboard/", dashboard_page),
    # path("dashboard/", can_detail),
    path("dashboard2/", can_detail),
    path("login/", login_page),
    path("signup/", signup_page),
    # path('candidateapi/', views.CandidateAPI.as_view()),


    path('', include(router.urls)),
    # path('add_user/', UserModelViewSet.add_user),
    # path('login_user/', UserModelViewSet.login_user),
]

# custom url
# companies/{companyid}/employees




# urlpatterns = [
    
#     path("backend/", include('backend.urls')),
    
# ]
