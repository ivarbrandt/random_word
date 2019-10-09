from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    if 'count' in request.session:
        request.session['count'] = request.session['count'] + 1
    else:
        request.session['count'] = 1
    
    request.session['string'] = get_random_string(length=15)

    return render(request, "random_word/index.html")

def reset(request):
    request.session.clear()
    return redirect('/ran_word')


# Create your views here.