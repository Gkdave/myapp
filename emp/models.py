from django.db import models

# Create your models here.
class Emp(models.Model):
    name= models.CharField(max_length=200)
    emp_id= models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    address= models.CharField(max_length=150)
    working= models.BooleanField(default=True)
    department= models.CharField(max_length=10)
    
    def __str__(self):
        return self.name
    
class Testimonial(models.Model):
    name = models.CharField(max_length=200)
    Testimonial = models.TextField()
    picture=models.ImageField(upload_to="testimonials/")
    rating = models.IntegerField(null=True)
    
    def __str__(self):
        return self.name 
    
    
class Feedback(models.Model):
        email=models.EmailField(max_length=100)
        name=models.CharField(max_length=100)
        feedback=models.TextField(max_length=200)
        
        def __str__(self):
            return self.name
        
    
    

