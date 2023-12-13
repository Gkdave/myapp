from django.contrib import admin

from .models import Emp , Testimonial ,Feedback
# Register your models here.

class EmpAdmin(admin.ModelAdmin):
    list_display=('name','working','phone','emp_id',)
    list_editable=('working','emp_id',)
    search_fields=('name','phone')
    list_filter=('working',)
    list_per_page=4 
    
    
    
admin.site.register(Emp)
admin.site.register(Testimonial)
admin.site.register(Feedback)


