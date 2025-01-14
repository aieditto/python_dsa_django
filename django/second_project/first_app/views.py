
from django.http import HttpResponse

# Create your views here.
def contact(request):
    return HttpResponse('''
                        <a href='#'>Contact</a>
                        <a href='/first_app/about/'>About</a>
                        <a href='/second_app/payment/'>Payment</a>
                        <a href='/second_app/details/'>Details</a>
                        <h1>from contact page</h1>
                        ''')

def about(request):
    return HttpResponse('''
                        <a href='/first_app/contact/'>Contact</a>
                        <a href='#'>About</a>
                        <a href='/second_app/payment/'>Payment</a>
                        <a href='/second_app/details/'>Details</a>
                        <h1>from about page</h1>
                        ''')