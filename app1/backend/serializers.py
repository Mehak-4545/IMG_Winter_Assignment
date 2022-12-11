from rest_framework import serializers
from backend.models import RecruitmentSeason,Round,Section,Question,Candidate,User,EvaluatorPanel,CandidateRound,CandidateQuestion

# create serializers here

class RecruitmentSeason(serializers.HyperlinkerModelSerializer):
    class Meta:
        model=RecruitmentSeason
        fields='__all__'


class Round(serializers.HyperlinkerModelSerializer):
    class Meta:
        model = Round
        fields = '__all__'


class Section(serializers.HyperlinkerModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'


class Question(serializers.HyperlinkerModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class Candidate(serializers.HyperlinkerModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'


class User(serializers.HyperlinkerModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class EvaluatorPanel(serializers.HyperlinkerModelSerializer):
    class Meta:
        model = EvaluatorPanel
        fields = '__all__'


class CandidateRound(serializers.HyperlinkerModelSerializer):
    class Meta:
        model = CandidateRound
        fields = '__all__'


class CandidateQuestion(serializers.HyperlinkerModelSerializer):
    class Meta:
        model = CandidateQuestion
        fields = '__all__'
