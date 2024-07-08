from django.http import HttpResponse
from django.shortcuts import render
from .forms import EmployeeForm

def homePage(request):
    return render(request,"index.html",)

# def userForms(request):
#     fn=userForms()

#     data={'form':fn}
#     return render(request,data)

def employee_data(request):
    form = EmployeeForm()
    return render(request,'main/employee.html',{'form':form})