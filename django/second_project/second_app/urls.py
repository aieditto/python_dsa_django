from django.urls import path
from . import views

urlpatterns = [
    path('payment/',views.payment),
    path('details/',views.details)
]
