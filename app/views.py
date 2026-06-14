from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm,TestimonialForm
from django.shortcuts import render, redirect
from .models import Testimonials,Work

# Create your views here.
def page1(request):
    data=Testimonials.objects.all().order_by('created_at')
    images_work=Work.objects.filter(show_on_home=True)
    
    if request.method == 'POST':
        if "contact_submit" in request.POST:
            form = ContactForm(request.POST)
            if form.is_valid():
                # 1. Save the data to the database
                contact_instance = form.save()

                # 2. Extract data for the email
                user_name = form.cleaned_data['name']
                user_email = form.cleaned_data['email']
            
                # 3. Send the email
                try:
                    send_mail(
                    subject=f'Thank You, {user_name}!',
                    message=f'Hi {user_name},\nI have received your Request. I will get back to you shortly.\n\nBest Regards,\nVicky',
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[user_email],
                    fail_silently=False)
                except Exception as e:
                    print(f"Email sending failed: {e}")
            
                # 4. Add a success message to display on the page
                messages.success(request, "Your message has been sent successfully! Check your email for confirmation.")
        
                form = ContactForm()
                return redirect("/#contact")
        elif "test_submit" in request.POST:
            t_form=TestimonialForm(request.POST)
            t_form.save()
            t_form= TestimonialForm()   
            return redirect("/#review")
    else:
    # GET request: Display an empty form
        form = ContactForm()
        t_form= TestimonialForm()
       
    return render(request, 'page1.html', {'form': form,'testimonials':data,'t_form':t_form,'images_work':images_work})

def work_images(request):

    correct_password = "wedding123"   # change this

    if request.method == "POST":
        entered_password = request.POST.get("password")

        if entered_password == correct_password:
            works = Work.objects.all()
            return render(request, 'work_images.html', {'works': works})
        else:
            return render(request, 'enter_password.html', {'error': "Please Enter Correct Password"})
            
   
    return render(request, "enter_password.html")
    

