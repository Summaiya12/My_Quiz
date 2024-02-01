from django.shortcuts import render
from .models import Category, Question
import requests


# Create your views here.
def About(request):
    return render(request, 'about.html')


def Contact(request):
    return render(request, 'contact.html')


def Index(request):
    return render(request, 'index.html')


def Quiz(request):
    categories = Category.objects.all()
    context = {'data': categories}

    return render(request, 'quiz.html', context)


def Result(request):
    return render(request, 'result.html')


def Login(request):
    return render(request, 'login.html')


def Register(request):
    return render(request, 'register.html')


def Ques(request, cat_id):
    category = Category.objects.get(id=cat_id)
    question = Question.objects.filter(category=category).order_by('id').first()
    quest = Question.objects.all()
    context = {
        "category": category,
        "question": question,
        "quest": quest

    }

    return render(request, 'ques.html', context)
