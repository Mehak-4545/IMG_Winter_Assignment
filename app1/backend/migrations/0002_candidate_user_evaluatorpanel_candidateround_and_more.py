# Generated by Django 4.1.1 on 2022-12-11 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('candidate_id', models.AutoField(primary_key=True, serialize=False)),
                ('enrollment_number', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
                ('cg', models.CharField(max_length=100)),
                ('current_status', models.CharField(max_length=100)),
                ('Recruitment_Season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.recruitment_season')),
                ('Round', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.round')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('enrollment_number', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('user_name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('dob', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='EvaluatorPanel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_id', models.CharField(max_length=100)),
                ('evaluator_id', models.CharField(max_length=100)),
                ('user_id', models.CharField(max_length=100)),
                ('Recruitment_Season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.recruitment_season')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.user')),
            ],
        ),
        migrations.CreateModel(
            name='CandidateRound',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_slot', models.CharField(max_length=100)),
                ('eval_status', models.CharField(max_length=100)),
                ('round_status', models.CharField(max_length=100)),
                ('Candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.candidate')),
                ('Round', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.round')),
            ],
        ),
        migrations.CreateModel(
            name='CandidateQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_score', models.CharField(max_length=100)),
                ('question_response', models.CharField(max_length=100)),
                ('panelist_remaks', models.CharField(max_length=100)),
                ('Candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.candidate')),
                ('Question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.question')),
            ],
        ),
    ]