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