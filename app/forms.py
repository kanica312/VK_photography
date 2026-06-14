from django import forms
from .models import Contact,Testimonials
from django.core.validators import RegexValidator

class ContactForm(forms.ModelForm):
    # Adding a phone number field with validation
    indian_phone_regex = RegexValidator(regex=r'^(\+91|0)?[6-9]\d{9}$',message="Please enter a valid Indian phone number.")
    phone_number = forms.CharField(validators=[indian_phone_regex],max_length=15, # Allow extra space for +91
    widget=forms.TextInput(attrs={'class': 'form-control bg-light p-3 border-0','placeholder': '9876543210'}))

    class Meta:
        model=Contact
        fields=['name','email','phone_number']
#css
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control bg-light p-3 border-0','placeholder':'Ex.John Doe'}),
            'email':forms.EmailInput(attrs={'class':'form-control bg-light p-3 border-0','placeholder':'name@example.com'}),
        }
from django import forms
from .models import Testimonials
class TestimonialForm(forms.ModelForm):
    class Meta:
        model=Testimonials
        fields=['name','message']
#css
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control bg-light p-3 border-0','placeholder':'Ex.John Doe'}),
            'message':forms.Textarea(attrs={'class':'form-control bg-light p-3 border-0','rows':4,'placeholder':'Type Your Message...'})
}