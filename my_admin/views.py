from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from section_office.models import OfficeDetails
from django.contrib import messages
from section_office.forms import OfficeForm
from log_manager.models import LoginDetails
# Create your views here.
class OfficeRegistration(View):
    def get(self,request):
        return render(request,'admin/office_registration.html')
    def post(self,request):
        data=OfficeForm(request.POST)
        if data.is_valid():
            username=request.POST.get('username')
            if LoginDetails.objects.filter(username=username).exists():
                messages.error(request,'username already exist')
                return render(request,'admin/office_registration.html')
            login_details=LoginDetails.objects.create_user(
                username=request.POST.get('username'),
                password=request.POST.get('password'),
                email=request.POST.get('email'),
                phone=request.POST.get('phone'),
                user_type='SECTION OFFICE'
            )
            details=data.save(commit=False)
            details.user_details=login_details
            details.save()
            messages.success(request,'registration sucessfull')
            return redirect('')
            
