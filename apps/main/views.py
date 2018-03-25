from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Course #import the database
# Create your views here.

def index(request):
    context = {
        'courses' : Course.objects.all()
    }
    return render(request, 'main/index.html', context)

def add(request):
        if request.method == "POST":
            # Validation
            errors = Course.objects.basic_validator(request.POST)
            if len(errors)>0:
                for tag, error in errors.iteritems():
                    messages.error(request, error)
            else:
                # Create a new record in the Course model database
                Course.objects.create(full_name=request.POST['full_name'], desc=request.POST['desc'])
        return redirect('../../')

def destroy(request,id):
    context = {
        'courses' : Course.objects.get(id=id)
    }
    return render(request, 'main/destroy.html', context)

def delete(request,id):
    if request.method == "POST" and request.POST.get('yes'):
        Course.objects.get(id=id).delete()
    return redirect('/')