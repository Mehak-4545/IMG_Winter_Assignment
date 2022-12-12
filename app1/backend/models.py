from django.db import models

# Create your models here.

class RecruitmentSeason(models.Model):
    season_id=models.AutoField(primary_key=True)
    year=models.CharField(max_length=100)


class Round(models.Model):
    round_id=models.AutoField(primary_key=True)
    role=models.CharField(max_length=100)
    type=models.CharField(max_length=100)

    RecruitmentSeason=models.ForeignKey(RecruitmentSeason,on_delete=models.CASCADE)

    # if record in parent table is deleted then record in child table will also be deleted


class Section(models.Model):
    section_id=models.AutoField(primary_key=True)
    section_name=models.CharField(max_length=100)
    role=models.CharField(max_length=100)
    total_questions=models.CharField(max_length=100)
    max_marks=models.CharField(max_length=100)

    Round=models.ForeignKey(Round,on_delete=models.CASCADE)


class Question(models.Model):
    question_id=models.AutoField(primary_key=True)
    question_statement=models.CharField(max_length=100)
    answer_type=models.CharField(max_length=100)
    answer=models.CharField(max_length=100)

    Section = models.ForeignKey(Section, on_delete=models.CASCADE)


class Candidate(models.Model):
    candidate_id=models.AutoField(primary_key=True)
    enrollment_number=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    branch=models.CharField(max_length=100)
    year=models.CharField(max_length=100)
    role=models.CharField(max_length=100)
    cg=models.CharField(max_length=100)
    current_status=models.CharField(max_length=100)

    RecruitmentSeason = models.ForeignKey(RecruitmentSeason, on_delete=models.CASCADE)
    Round = models.ForeignKey(Round, on_delete=models.CASCADE)




class CandidateRound(models.Model):
    time_slot=models.CharField(max_length=100)
    eval_status=models.CharField(max_length=100)
    round_status=models.CharField(max_length=100)

    Round = models.ForeignKey(Round, on_delete=models.CASCADE)
    Candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    enrollment_number=models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    role=models.CharField(max_length=100)
    year=models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    user_name=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    # dob=models.CharField(max_length=100)



class EvaluatorPanel(models.Model):
    parent_id=models.CharField(max_length=100)
    evaluator_id=models.CharField(max_length=100)
    user_id=models.CharField(max_length=100)
    

    RecruitmentSeason= models.ForeignKey(RecruitmentSeason, on_delete=models.CASCADE)

    User = models.ForeignKey(User, on_delete=models.CASCADE)


class CandidateQuestion(models.Model):
    question_score=models.CharField(max_length=100)
    question_response=models.CharField(max_length=100)
    panelist_remaks=models.CharField(max_length=100)

    Candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    Question = models.ForeignKey(Question, on_delete=models.CASCADE)







