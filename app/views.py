from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *
def student(request):
    SFO=StudentForm()
    d={'SFO':SFO}

    if request.method=='POST':
        SFD=StudentForm(request.POST)
        if SFD.is_valid():
            sid=SFD.cleaned_data['sid']
            name=SFD.cleaned_data['name']
            email=SFD.cleaned_data['email']
            SO=Student.objects.get_or_create(sid=sid,name=name,email=email)[0]
            SO.save()
            
            SQS=Student.objects.all()
            d1={'SQS':SQS}
            return render(request,'display_student.html',d1)

    return render(request,'student.html',d)

def display_topic(request):
    TFO=TopicForm()
    d={'TFO':TFO}

    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFD.is_valid():
            TFDO.save()

            return HttpResponse('Topic insertion is successfull')

    return render(request,'display_topic.html',d)