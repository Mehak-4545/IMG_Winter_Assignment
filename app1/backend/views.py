from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import RecruitmentSeason, Round, Section, Question, Candidate, User, EvaluatorPanel, CandidateRound, CandidateQuestion
from .serializers import RecruitmentSeasonSerializer, RoundSerializer, SectionSerializer, QuestionSerializer, CandidateSerializer, UserSerializer, EvaluatorPanelSerializer, CandidateRoundSerializer, CandidateQuestionSerializer
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
        # return HttpResponse('<h1>dummy user registered</h1>')

        if request.method=="POST":

            #data fetch
            mem_name=request.POST.get("mem_name")
            mem_enum=request.POST.get("mem_enum")
            mem_email=request.POST.get("mem_email")
            mem_phone=request.POST.get("mem_phone")
            mem_role=request.POST.get("mem_role")
            mem_year=request.POST.get("mem_year")
            mem_dept=request.POST.get("mem_dept")
            mem_username=request.POST.get("mem_username")
            mem_pw=request.POST.get("mem_pw")
            # mem_cpw=request.POST.get("mem_cpw")

            #create model object and set data
            m = User()
            m.name = mem_name
            m.enrollment_number = mem_enum
            m.email = mem_email
            m.phone_number = mem_phone
            m.role = mem_role
            m.year = mem_year
            m.branch = mem_dept
            m.user_name = mem_username
            m.password = mem_pw

            # Validate

            # save object
            m.save()

            # prepare message
            print("User being created")

            return redirect("/backend/add_user/")

        return HttpResponse('<h1>dummy user registered</h1>')
        return render(request, "signup.html", {})

            

    def login_user(request):
        print('this action will login an existing user')
        return HttpResponse('<h1>dummy user logged in</h1>')


class EvaluatorPanelViewSet(viewsets.ModelViewSet):
    serializer_class = EvaluatorPanelSerializer
    queryset = EvaluatorPanel.objects.all()


class CandidateRoundViewSet(viewsets.ModelViewSet):
    serializer_class = CandidateRoundSerializer
    queryset = CandidateRound.objects.all()


class CandidateQuestionViewSet(viewsets.ModelViewSet):
    serializer_class = CandidateQuestionSerializer
    queryset = CandidateQuestion.objects.all()
