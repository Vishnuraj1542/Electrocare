from django.shortcuts import render,redirect,get_object_or_404
from django.views import View

# Create your views here.
class UserPage(View):
    def get(self,request):
        return render(request,'user/home.html')
class AdminPage(View):
    def get(self,request):
        return render(request,'admin/homepage.html')
class LinemanPage(View):
    def get(self,request):
        return render(request,'worker/homepage.html')
class SubstationPage(View):
    def get(self,request):
        return render(request,'substation/homepage.html')
