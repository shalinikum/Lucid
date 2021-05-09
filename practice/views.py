from django.shortcuts import render
from django.http import HttpResponse
from practice.models import User, UserTask , WordsAttribute, Word
import random

def index(request):
    return HttpResponse("Hello, world. Let's practice.")

def fetch_user_task(request,user_id):
    tasks = UserTask.objects.filter(user_id=user_id)
    return render(request, "task_list.html",{'tasks' : tasks})

def fetch_words(request,attribute_id):
    words = Word.objects.filter(attribute_id = attribute_id )
    random_words = random.sample(list(words) ,2)
    print(random_words)
    return render(request, "word_list.html",{'words' : random_words})