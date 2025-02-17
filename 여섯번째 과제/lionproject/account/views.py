from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .forms import RegisterForm
# Create your views here.


def login_view(request): #로그인 창을 띄우는 함수

    if request.method == "POST":
        form = AuthenticationForm(request = request, data= request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username") #cleaned_data 유효성 검사에 통과된 깨끗한 데이터
            password = form.cleaned_data.get("password")
            user = authenticate(request = request, username= username, password=password)
            if user is not None:
                login(request, user)
        return redirect("home")

    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form':form})


def logout_view(request):
    logout(request)
    return redirect("home")

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect("home")
    else:
        form = RegisterForm()
        return render(request, 'signup.html', {'form':form})