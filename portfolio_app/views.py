from django.shortcuts import render
from .models import Profile, Project, Skill, Certificate, Contact, Education
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect, render



def home(request):
    profile = Profile.objects.first()
    projects = Project.objects.all()
    skills = Skill.objects.all()
    certificates = Certificate.objects.all()
    education = Education.objects.all()
    contact = Contact.objects.first()  # Fetch the first contact entry (or you can fetch a specific one if needed)
    success = None  # Initialize success to None

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Construct the email message
        subject = f"Contact Form Submission from {name}"
        email_message = f"Name: {name}\nEmail: {email}\nMessage:\n{message}"
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = 'salehalkhalafat144@gmail.com'  # The email address to receive the form submissions

        # Send the email
        try:
            send_mail(subject, email_message, from_email, [to_email])
            success = True
            messages.success(request, 'Your message was sent successfully.')
            return redirect('home')  # Redirect to the same view with a different URL
        except Exception as e:
            # Handle any errors that occur during sending
            print(f"Error sending email: {e}")
            success = False
            messages.error(request, 'An error occurred while sending your message.')
            return render(request, 'home', {'success': success})


    return render(request, 'portfolio_app/home.html', {
        'profile': profile,
        'projects': projects,
        'educations': education,
        'skills': skills,
        'certificates': certificates,
        'contact': contact
        })
