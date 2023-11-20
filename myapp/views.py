from django.http import HttpResponse
from django.shortcuts import render

import datetime 


date = datetime.datetime.now()

def home(request):


    print ('test Function is called from views')
    return HttpResponse('This is index page it is now: date' + str(date))