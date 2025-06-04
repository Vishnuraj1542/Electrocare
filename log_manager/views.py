from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.views import View
from .models import LoginDetails
from django.contrib import messages

# Create your views here.
def admin_page(request):
    return render(request,'admin/admin_page.html')
def office_page(request):
    return render(request,'office/office_page.html')
def public_page(request):
    return render(request,'public/public_Page.html')
def worker_page(request):
    return render(request,'worker/worker_page.html')

class Login(View):
    def get(self,request):
        return render(request,'login/login.html')
    
    def post(self,request):
        landing_url={
            'Admin':'log_manager:admin_page',
            'Public':'log_manager:public_page',
            'Worker':'log_manager:worker_page',
            'Office':'log_manager:office_page',
        }
        username=request.POST.get('username')
        password=request.POST.get('password')
        if not LoginDetails.objects.filter(username=username).exists():
            messages.error(request,'user not found')
            return render(request,'login/login.html')
        user=authenticate(request,username=username,password=password)
        if user is None:
            print('user is none')
            messages.error(request,'invalid username or password')
            return render(request,'login/login.html')
        login(request,user)
        print(request.user)
        user_type=request.user.user_type
        if user_type in landing_url:
            messages.success(request,'logged in sucessfully')
            return redirect(landing_url.get(user_type))
        return render(request,'login/login.html',{'user':user})
            

            

          
            