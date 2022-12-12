from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import datetime


def home_page(request):
    # date = datetime.datetime.now()

    print("home page requested")
    # return JsonResponse(friends,safe=False)
    # return HttpResponse("This is home page")
    return render(request,"home.html",{})


def profile_page(request):
    # date = datetime.datetime.now()

    print("profile page requested")
    # return JsonResponse(friends,safe=False)
    # return HttpResponse("This is home page")
    return render(request, "profile.html", {})



def dashboard_page(request):
    # date = datetime.datetime.now()

    print("dashboard page requested")
    # return JsonResponse(friends,safe=False)
    # return HttpResponse("This is home page")
    return render(request, "dashboard.html", {})


def login_page(request):
    # date = datetime.datetime.now()

    print("login page requested")
    # return JsonResponse(friends,safe=False)
    # return HttpResponse("This is home page")
    return render(request, "login.html", {})


def signup_page(request):
    # date = datetime.datetime.now()

    print("signup page requested")
    # return JsonResponse(friends,safe=False)
    # return HttpResponse("This is home page")
    return render(request, "signup.html", {})


