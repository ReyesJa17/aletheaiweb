from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Email subject and message
            subject = f"New contact from {name}"
            email_message = f"From: {name}\nEmail: {from_email}\n\nMessage:\n{message}"

            send_mail(subject, email_message, from_email, ['testcluster7u7@gmail.com'])

            # Redirect to the success page after sending the email
            return redirect('success')  # Make sure 'success' is a named URL in your urls.py
    else:
        form = ContactForm()

    return render(request, 'home/contact.html', {'form': form})

def home(request):
    return render(request, 'home/home.html')

def projects(request):
    return render(request, 'home/projects.html')

def services(request):
    return render(request, 'home/services.html')

def about(request):
    return render(request, 'home/about.html')

def success(request):
    return render(request, 'home/ContactSuccess.html')

