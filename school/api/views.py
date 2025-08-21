from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import auto_redirect, role_required
from .models import Student, Teacher, Result, User   # <-- apne models import karo
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import RegisterSerializer

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return auto_redirect(user)
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'login.html')



class RegisterView(APIView):
    def get(self,request):
        return render(request,'register.html')
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # ✅ after successful register → redirect to login page
            return redirect('login') 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@login_required
@role_required(['principal'])
def principal_dashboard(request):
    students = Student.objects.all()
    teachers = Teacher.objects.all()
    results = Result.objects.all()
    return render(request, 'principal_dashboard.html', {
        'students': students,
        'teachers': teachers,
        'results': results
    })


@login_required
@role_required(['teacher'])
def teacher_dashboard(request):
    teacher = Teacher.objects.get(user=request.user)   # teacher ka record
    results = Result.objects.filter(student__class_name="10A")  # Example: apne students ke results
    return render(request, 'teacher_dashboard.html', {
        'teacher': teacher,
        'results': results
    })


@login_required
@role_required(['student'])
def student_dashboard(request):
    student = Student.objects.get(user=request.user)
    results = Result.objects.filter(student=student)
    return render(request, 'student_dashboard.html', {
        'student': student,
        'results': results
    })


@login_required
def default_dashboard(request):
    return render(request, 'default_dashboard.html')
