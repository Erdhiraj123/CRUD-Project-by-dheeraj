from django.shortcuts import render
from . forms import StudentRegistration,TeacherRegistration
from . models import User

# Create your views here.
def student(request):
    if request.method=="POST":
        fm=StudentRegistration(request.POST)                                    
        if fm.is_valid():
            fm.save()
    else:
        fm= StudentRegistration()
    return render(request, 'student.html',{'form':fm})

def teacher(request):
    if request.method=='POST':
        fm=TeacherRegistration(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm= TeacherRegistration()
    return render(request,'teacher.html',{'form':fm})