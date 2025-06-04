from django.shortcuts import render,redirect
from django.contrib import messages
from django.views import View
from .forms import OfficeForm
from log_manager.models import LoginDetails

# Create your views here.
class OfficeRegistration (View):
    def get(self,request):
        return render(request,'admin/office_registration.html')
    def post(self,request):
        data = OfficeForm(request.POST)
        if data.is_valid():
            username= request.POST.get('username'),
            if not LoginDetails.objects.filter(username=username).exists():
                details=LoginDetails.objects.create_user(
                username= request.POST.get('username'),
                password= request.POST.get('password'),
                phone=request.POST.get('phone'),
                user_type='Office'
                )
                form=data.save(commit=False)
                form.user_details=details
                form.save()
                messages.success(request,'section office added sucessfully')
                return redirect('log_manager:admin_page')
            messages.error(request,'user already registered')
            return render(request,'admin/office_registration.html')
        return render(request,'admin/office_registration.html',{'form':form})
