from django.shortcuts import render
from rest_framework import viewsets
from backend.models import RecruitmentSeason, Round, Section, Question, Candidate, User, EvaluatorPanel, CandidateRound, CandidateQuestion
from backend.serializers import RecruitmentSeasonSerializer, RoundSerializer, SectionSerializer, QuestionSerializer, CandidateSerializer, UserSerializer, EvaluatorPanelSerializer, CandidateRoundSerializer, CandidateQuestionSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import HttpResponse

# # Create your views here.


class RecruitmentSeasonViewSet(viewsets.ModelViewSet):
    serializer_class = RecruitmentSeasonSerializer
    queryset=RecruitmentSeason.objects.all()


class RoundViewSet(viewsets.ModelViewSet):
    serializer_class = RoundSerializer
    queryset = Round.objects.all()


class SectionViewSet(viewsets.ModelViewSet):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()


class CandidateViewSet(viewsets.ModelViewSet):
    serializer_class = CandidateSerializer
    queryset = Candidate.objects.all()


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def add_user(request):
        print('this action will add a user')
        return HttpResponse('<h1>dummy user registered</h1>')


class EvaluatorPanelViewSet(viewsets.ModelViewSet):
    serializer_class = EvaluatorPanelSerializer
    queryset = EvaluatorPanel.objects.all()


class CandidateRoundViewSet(viewsets.ModelViewSet):
    serializer_class = CandidateRoundSerializer
    queryset = CandidateRound.objects.all()


class CandidateQuestionViewSet(viewsets.ModelViewSet):
    serializer_class = CandidateQuestionSerializer
    queryset = CandidateQuestion.objects.all()
