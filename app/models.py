from django.db import models


# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=200)
    phone_number=models.CharField(max_length=14)
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=['-created_at']
    def __str__(self):
        return f'{self.name}-{self.created_at.strftime("%Y-%m-%d")}'

class Testimonials(models.Model):
    
    name=models.CharField(max_length=50)
    message=models.TextField(max_length=200)
  
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        #ordering results
        ordering=['-created_at']
    def __str__(self):
        return f'Testimonial by {self.name} - added on {self.created_at.strftime("%Y-%m-%d")}'

class Work(models.Model):
    images=models.ImageField(upload_to='work/',null=True,blank=True)  
    created_at=models.DateTimeField(auto_now_add=True)  
    show_on_home=models.BooleanField(default=False)
    class Meta:
        #ordering results
        ordering=['created_at']
    def __str__(self):
        return f'added on {self.created_at.strftime("%Y-%m-%d")}'
            