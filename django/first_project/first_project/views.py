from django.http import HttpResponse

def home(request):
    return HttpResponse('Hello Shakalaka Boom Boom')

def about(request):
    return HttpResponse("From About Page")