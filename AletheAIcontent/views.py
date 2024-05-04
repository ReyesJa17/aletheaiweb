from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import MediaFile
from .models import Image

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


def upload_media(request):
    if request.method == 'POST' and request.FILES['file']:
        media_file = MediaFile(name=request.FILES['file'].name, file=request.FILES['file'])
        media_file.save()
        return redirect('media_list')
    return render(request, 'upload_media.html')

def home(request):
    try:
        logo = Image.objects.get(name='logo')
        robot1 = Image.objects.get(name='robot1')
        robot2 = Image.objects.get(name='robot2')
        robot3 = Image.objects.get(name='robot3')
        robot4 = Image.objects.get(name='robot4')
        reloj = Image.objects.get(name='reloj')
        asistencia = Image.objects.get(name='asistencia')
        mai = Image.objects.get(name='mai')
        market = Image.objects.get(name='market')
        cerveceria = Image.objects.get(name='cerveceria')
        tiktok = Image.objects.get(name='tiktok')
        futuro = Image.objects.get(name='futuro')
        
    except Image.DoesNotExist:
        logo = None
        robot1 = None
        robot2 = None
        robot3 = None
        robot4 = None
        reloj = None
        asistencia = None
        mai = None
        market = None
        cerveceria = None
        tiktok = None
        futuro = None
  
    context = {
        'logo': logo,
        'robot1': robot1,
        'robot2': robot2,
        'robot3': robot3,
        'robot4': robot4,
        'reloj': reloj,
        'asistencia': asistencia,
        'mai': mai,
        'market': market,
        'cerveceria': cerveceria,
        'tiktok': tiktok,
        'futuro': futuro,
   
    }
    return render(request, 'home/home.html', context)

def contact(request):
    try:
        logo = Image.objects.get(name='logo')
        robot5 = Image.objects.get(name='robot5')
    except Image.DoesNotExist:
        robot5 = None
        logo = None
    context = {
        'logo': logo,
        'robot5': robot5,
    }
    return render(request, 'home/contact.html', context)

def about(request):
    try:
        logo = Image.objects.get(name='logo')
        info = Image.objects.get(name='info')
        edificios = Image.objects.get(name='edificios')
    except Image.DoesNotExist:
        logo = None
        info = None
        edificios = None
    context = {
        'logo': logo,
        'info': info,
        'edificios': edificios,
    }
    return render(request, 'home/about.html', context)

def services(request):
    try:
        logo = Image.objects.get(name='logo')
        mai = Image.objects.get(name='mai')
        school = Image.objects.get(name='school')
        chef = Image.objects.get(name='chef')
        mensaje = Image.objects.get(name='mensaje')
        poli = Image.objects.get(name='poli')
        mercado = Image.objects.get(name='mercado')
        ask = Image.objects.get(name='ask')
        cerveceria = Image.objects.get(name='cerveceria')
    except Image.DoesNotExist:
        logo = None
        mai = None
        school = None
        chef = None
        mensaje = None
        poli = None
        mercado = None
        ask = None
        cerveceria = None

    context = {
        'logo': logo,
        'mai': mai,
        'school': school,
        'chef': chef,
        'mensaje': mensaje,
        'poli': poli,
        'mercado': mercado,
        'ask': ask,
        'cerveceria': cerveceria,
    }
    return render(request, 'home/services.html', context)