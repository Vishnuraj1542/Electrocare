from django.shortcuts import render,redirect
from django.contrib import messages
from django.views import View
from .forms import OfficeForm
from log_manager.models import LoginDetails

# Create your views here.
class OfficeRegistration (View):
    def get(self,request):
        return render(request,'office_registration.html')
    def post(self,request):
        data = OfficeForm(request.POST)
        if data.is_valid():
            user=LoginDetails.objects.create(
            username= request.POST.get('username'),
            password= request.POST.get('password'),
            phone=request.POST.get('phone'),
            user_type='Office'
        )
            form=data.save(commit=False)
            user_details=data
            form.save()
            messages.success(request,'section office added sucessfully')
            return redirect('adminpage')
        return render(request,'office_registration.html',{'form':form})
