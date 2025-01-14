from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def payment(request):
    return HttpResponse('''
                        <a href='/first_app/contact/'>Contact</a>
                        <a href='/first_app/about/'>About</a>
                        <a href='#'>Payment</a>
                        <a href='/second_app/details/'>Details</a>
                        <h1>from payment page</h1>
                        ''')

def details(request):
    return HttpResponse('''
                        <a href='/first_app/contact/'>Contact</a>
                        <a href='/first_app/about/'>About</a>
                        <a href='/second_app/payment/'>Payment</a>
                        <a href='#'>Details</a>
                        <h1>from details page</h1>
                        ''')