from django.http import HttpResponse
from django.shortcuts import render

import datetime 




def home(request):
    isActive = True 
    if request.method == "POST":
        check = request.POST.get("check")
        print(check)
        if check is None: isActive =False 
        else: isActive=True 
        name = request.POST.get("name")
        print(name)
        
    date = datetime.datetime.now()
    
    name = "Rahul"
    list_of_programs=[
        'WAP to check even or odd',
        'WAP to check prime number',
        'WAP to print all prime numbers form 1 to 100',
        'Wap to print pascals triangle'
        
    ]
    student={
        'student_name':'Rahul',
        'student_college':'xyz',
        'student_city':'Udaipur',
    }
    data={
        'date':date,
        'isActive':isActive,
        'name':name,
        'list_of_programs':list_of_programs,
        'student_data':student,
    }
    

    # print ('test Function is called from views')
    # return HttpResponse('This is index page it is now: date' + str(date))
    return render(request,"home.html",data)

def about(request):
    return render(request,"about.html",{})

def services(request):
    return render(request,"services.html",{})