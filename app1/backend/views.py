from django.shortcuts import render, redirect
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from .models import RecruitmentSeason, Round, Section, Question, Candidate, User, EvaluatorPanel, CandidateRound, CandidateQuestion
from .serializers import RecruitmentSeasonSerializer, RoundSerializer, SectionSerializer, QuestionSerializer, CandidateSerializer, UserSerializer, EvaluatorPanelSerializer, CandidateRoundSerializer, CandidateQuestionSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from rest_framework import viewsets

from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAdminUser # (staff=true)

# # Create your views here.

def can_detail(request):
        emps=Candidate.objects.all()
        # return render(request, "dashboard.html", {'emps' :emps})
        return render(request, "dashboard2.html", {'emps' :emps})



class RecruitmentSeasonModelViewSet(viewsets.ModelViewSet):
    queryset=RecruitmentSeason.objects.all()
    serializer_class = RecruitmentSeasonSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]

    


class RoundModelViewSet(viewsets.ModelViewSet):
    serializer_class = RoundSerializer
    queryset = Round.objects.all()
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]



class SectionModelViewSet(viewsets.ModelViewSet):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]



class QuestionModelViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]



class CandidateModelViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]



    

class UserModelViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]


    # def add_user(request):
    #     print('this action will add a user')
    #     # return HttpResponse('<h1>dummy user registered</h1>')

    #     if request.method=="POST":

    #         #data fetch
    #         mem_name=request.POST.get("mem_name")
    #         mem_enum=request.POST.get("mem_enum")
    #         mem_email=request.POST.get("mem_email")
    #         mem_phone=request.POST.get("mem_phone")
    #         mem_role=request.POST.get("mem_role")
    #         mem_year=request.POST.get("mem_year")
    #         mem_dept=request.POST.get("mem_dept")
    #         mem_username=request.POST.get("mem_username")
    #         mem_pw=request.POST.get("mem_pw")
    #         # mem_cpw=request.POST.get("mem_cpw")

    #         #create model object and set data
    #         m = User()
    #         m.name = mem_name
    #         m.enrollment_number = mem_enum
    #         m.email = mem_email
    #         m.phone_number = mem_phone
    #         m.role = mem_role
    #         m.year = mem_year
    #         m.branch = mem_dept
    #         m.user_name = mem_username
    #         m.password = mem_pw

    #         # Validate

    #         # save object
    #         m.save()

    #         # prepare message
    #         print("User being created")

    #         return redirect("/backend/add_user/")

    #     # return HttpResponse('<h1>dummy user registered</h1>')
    #     return render(request, "signup.html", {})

            

    # def login_user(request):
    #     print('this action will login an existing user')
    #     return HttpResponse('<h1>dummy user logged in</h1>')


class EvaluatorPanelModelViewSet(viewsets.ModelViewSet):
    serializer_class = EvaluatorPanelSerializer
    queryset = EvaluatorPanel.objects.all()
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]



class CandidateRoundModelViewSet(viewsets.ModelViewSet):
    serializer_class = CandidateRoundSerializer
    queryset = CandidateRound.objects.all()
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]



class CandidateQuestionModelViewSet(viewsets.ModelViewSet):
    serializer_class = CandidateQuestionSerializer
    queryset = CandidateQuestion.objects.all()
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]




# @method_decorator(csrf_exempt, name='dispatch')
# class CandidateAPI(View):

#     def get(self, request, *args, **kwargs):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         candidate_id = pythondata.get('candidate_id', None)
#         if candidate_id is not None:
#             stu = Candidate.objects.get(candidate_id=candidate_id)
#             serializer = stu = CandidateSerializer(stu)
#             json_data = JSONRenderer().render(serializer.data)
#             return HttpResponse(json_data, content_type='application/json')

#         else:
#             stu = Candidate.objects.all()
#             serializer = stu = CandidateSerializer(stu)
#             json_data = JSONRenderer().render(serializer.data)
#             return HttpResponse(json_data, content_type='application/json')



#     def post(self, request, *args, **kwargs):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         serializer = CandidateSerializer(data = pythondata)

#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg' : 'Data Created'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='Application/json')

#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type='Application/json')




#     def put(self, request, *args, **kwargs):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         candidate_id = pythondata.get('candidate_id')
#         stu = Candidate.objects.get(candidate_id=candidate_id)
#         serializer = stu = CandidateSerializer(stu,data = pythondata,partial=True)

#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg' : 'Data Updated'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='Application/json')

#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type='Application/json')




#     def delete(self, request, *args, **kwargs):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         candidate_id = pythondata.get('candidate_id')
#         stu = Candidate.objects.get(candidate_id=candidate_id)
#         stu.delete()

#         res = {'msg : Data Deleted'}
#         json_data = JSONRenderer().render(res)
#         return HttpResponse(json_data, content_type='Application/json')
 
