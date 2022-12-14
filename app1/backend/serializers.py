from rest_framework import serializers
from backend.models import RecruitmentSeason,Round,Section,Question,Candidate,User,EvaluatorPanel,CandidateRound,CandidateQuestion

# create serializers here


class RecruitmentSeasonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=RecruitmentSeason
        fields='__all__'


class RoundSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Round
        fields = '__all__'


class SectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class CandidateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Candidate
        fields = ('candidate_id','enrollment_number','name','email','phone','branch','year','role','cg','current_status')
        # fields = ('candidate_id','enrollment_number','name','email','phone','branch','year','role','cg','current_status','RecruitmentSeason','Round')
        # extra_kwargs = {}


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class EvaluatorPanelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EvaluatorPanel
        fields = '__all__'


class CandidateRoundSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CandidateRound
        fields = '__all__'


class CandidateQuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CandidateQuestion
        fields = '__all__'
