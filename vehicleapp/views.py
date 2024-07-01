from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from vehicleapp.models import VehicleModel
from django.views import View
from vehicleapp.forms import UserRegistrationForm,UserLoginForm
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout

# Create your views here.
class HomeView(View):
    def get(self,request):
        return render(request,'index.html')
class UserHome(View):
    def get(self,request):
        return render(request,'userhome.html')

class UserRegisterView(View):
    def get(self,request):
        form=UserRegistrationForm()
        return render(request,'register.html',{'form':form})
    def post(self,request):
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            formdata=form.cleaned_data
            VehicleModel.objects.create_user(**formdata)
            return HttpResponse("Registered")
        else:
            return HttpResponse("inavild")
        
class UserLoginView(View):
    def get(self,request):
        form=UserLoginForm()
        return render(request,'login.html',{'form':form})
    def post(self,request):
        uname=request.POST.get("username")
        psw=request.POST.get("password")
        user=authenticate(request,username=uname,password=psw)
        if user:
            login(request,user)
            return redirect('user_home')
        else:
            return redirect('home_view')
        
class UserlogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('home_view')


class UserProfileView(View):
    def get(self,request,*args, **kwargs):
        user=VehicleModel.objects.filter(username=request.user)
        print(user)
        return render(request,'Userprofile.html',{'data':user})
        

            
        
    
    
        
    
    
