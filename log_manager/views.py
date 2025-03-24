from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from .models import LoginDetails
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
class UserPage(View):
    def get(self,request):
        return render(request,'user/homepage.html')
class AdminPage(View):
    def get(self,request):
        return render(request,'admin/homepage.html')
class WorkerPage(View):
    def get(self,request):
        return render(request,'worker/homepage.html')
class OfficePage(View):
    def get(self,request):
        return render(request,'substation/homepage.html')
    
class Login(View):
    def get(self,request):
        return render(request,'log_manager/login.html')
    def post(self,request):
        username=request.POST.get('username')
        password=request.POST.get('password')
        response_dict={"success":False}
        user=authenticate(username=username,password=password)
        if user is None:
            response_dict['reason']="Invalid Credential"
            messages.error(request,response_dict['reason'])
            return render(request,'log_manager,login.html',{'logerror':response_dict['reason']})
        login(request,user)
        landing_url={
            'ADMIN':'log_manager:adminhome',
            'PUBLIC':'log_manager:userhome',
            'WORKER':'log_manager:'
        }
            
   
   
        
