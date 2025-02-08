from django.urls import path
from .import views 

urlpatterns=[
    path('contact/',views.contact, name="contact"),
    path('forminfo/',views.form, name="form"), 
    path('djangoform/',views.django_form,name='django_form')
]