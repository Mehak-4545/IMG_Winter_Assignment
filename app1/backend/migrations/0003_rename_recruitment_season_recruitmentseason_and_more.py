# Generated by Django 4.1.1 on 2022-12-11 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_candidate_user_evaluatorpanel_candidateround_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Recruitment_Season',
            new_name='RecruitmentSeason',
        ),
        migrations.RenameField(
            model_name='candidate',
            old_name='Recruitment_Season',
            new_name='RecruitmentSeason',
        ),
        migrations.RenameField(
            model_name='evaluatorpanel',
            old_name='Recruitment_Season',
            new_name='RecruitmentSeason',
        ),
        migrations.RenameField(
            model_name='round',
            old_name='Recruitment_Season',
            new_name='RecruitmentSeason',
        ),
    ]