from django.contrib import admin
from .models import Candidate

# Register your models here.


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ['candidate_id','enrollment_number','name','email','phone','branch','year','role','cg','current_status']
    # list_display = ['candidate_id','enrollment_number','name','email','phone','branch','year','role','cg','current_status','RecruitmentSeason','Round']


class UserAdmin(admin.ModelAdmin):
    lisy_display = ['usre_id','name','enrollment_number','email','phone_number','role','year''branch','usre_name','password']