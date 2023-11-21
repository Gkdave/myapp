from django.contrib import admin
from django.urls import path
from . views import  *

urlpatterns = [
    
    path('home/',employee),
    path('add-emp/',add_emp),
    path('delete-emp/<int:emp_id>',delete_emp),
    path('update-emp/<int:emp_id>',update_emp),
]
