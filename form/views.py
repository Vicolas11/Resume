from form.models import ContactModel
from django.shortcuts import redirect, render
from django.contrib import messages
from django.core.mail import send_mail  
from django.conf import settings

# Create your views here.
def contact_form(request, *args, **kwargs): 
    # Let Us Check if the person has submitted with an email before
    if request.method == 'POST':
        queryset = ContactModel.objects.filter(email=request.POST.get('email'))
        if not queryset.exists():
            name_ = request.POST.get('name')
            email_ = request.POST.get('email')
            subject_ = request.POST.get('subject'),
            message_ = request.POST.get('message')
            #Post to Database
            ContactModel.objects.create(
                name = name_,
                email = email_,
                subject = subject_,
                message = message_
            )
            #Sent email to the person's GMAIL Account
            subject = "Contact Form"  
            msg     = "Hello\nWe have sucessfully received your request.\nThanks."  
            to      = email_
            res     = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])  
            
            if(res == 1):  
                messages.success(request, 'Contact Form submitted successfully! Check your GMail')
            else:  
                messages.debug(request, 'Mail could not sent')                        
        else:
            messages.error(request, 'Sorry you have submitted with this email already!')

    return redirect('index')