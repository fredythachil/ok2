from django.shortcuts import render

# Create your views here.
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Student, Branch,Purpose
from .forms import StudentForm
from django.shortcuts import render, redirect


class StudentListView(ListView):
    model = Student
    form_class = StudentForm
    context_object_name = 'students'

def StudentCreateView(request):

    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,'Submitted Successfully')
    return render(request,'ok.html',{'form':form})
    # success_url = reverse_lazy('student_changelist')

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('student_changelist')

def load_branches(request):
    department_id = request.GET.get('department')
    branches = Branch.objects.filter(department_id=department_id).order_by('name')


    return render(request, 'course_dropdown.html', {'branches': branches})
# def load_course(request):
#     department_id=request.GET.get('department')
#     courses=Course.objects.filter(department_id=department_id).order_by('name')
#     return render(request,'course_dropdown.html',{'course':courses})


# def load_course(request):
#     department_id = request.GET.get('department_id')
#     course = Course.objects.filter(department_id=department_id).all()
#     return render(request, 'course_dropdown.html', {'courses': course})


def a(request):
    return render(request,'index.html')


def loginn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('student_add')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    return render(request, 'login.html')


# class dep(CreateView):
#     model=select
#     template_name = 'ok.html'
#     fields = '__all__'
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'password does not match')
            return redirect('register')
    return render(request, 'register.html')


def logoutt(request):
    auth.logout(request)
    return redirect('/')


