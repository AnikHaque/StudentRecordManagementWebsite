from django.shortcuts import render, HttpResponse
from . import models

# Create your views here.
def home(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        phone=request.POST.get('phone')
        checkbox=request.POST.get('checkbox')

        if checkbox == 'on':
            checkbox=True

        else:
            checkbox=False

        student = models.Student(name=name,email=email,phone=phone,password=password,checkbox=checkbox)
        student.save()
        return HttpResponse("Student Object Created Successfully")


    return render(request,'student/index.html')