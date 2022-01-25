from django.shortcuts import render
from time import strftime, localtime

# Create your views here.
def index(request):
    context = {
        "time": strftime("%m-%d-%Y %H:%M %p", localtime())
    }
    return render(request, 'index.html', context)