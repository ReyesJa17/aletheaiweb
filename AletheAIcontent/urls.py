from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Points to the home view
    path('projects/', views.projects, name='projects'),  # Points to the projects view
    path('services/', views.services, name='services'),  # Points to the services view
    path('about/', views.about, name='about'),  # Points to the about view
    path('contact/', views.contact, name='contact'),  # Points to the contact view
    path('success/', views.success, name='success') , # Points to the contact_success view
    path('terms/', views.terms, name='terms'),  # Points to the terms view
    path('privacy/', views.privacy, name='privacy')  # Points to the privacy view

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


