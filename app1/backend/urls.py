# no use
# 

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

    path('', include(router.urls)),
    # path('add_user/', UserModelViewSet.add_user),
    # path('login_user/', UserModelViewSet.login_user),
]

# custom url
# companies/{companyid}/employees
