from django.http import HttpResponse

def home(request):
    return HttpResponse('From Apps Home')
def contact(request):
    return HttpResponse('From Contact Page')