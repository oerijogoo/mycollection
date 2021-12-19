from django.urls import path
from clinic.views import About, Home, Contact

urlpatterns = [
    path('', Home, name='home'),
    path('about/', About, name='about'),
    path('contact/', Contact, name='contact'),

]