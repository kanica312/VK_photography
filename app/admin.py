from django.contrib import admin

# Register your models here.
from .models import Contact,Testimonials,Work
admin.site.register(Contact)
admin.site.register(Testimonials)
admin.site.register(Work)
