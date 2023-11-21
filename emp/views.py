from django.shortcuts import render
from .models import Emp 

def employee(request):
    emps = Emp.objects.all()
    return render(request,"employee.html",{'emps':emps})