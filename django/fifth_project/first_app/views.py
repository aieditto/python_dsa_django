from django.shortcuts import render

# Create your views here.
def contact(request):
        return render(request,'first.html')

def form(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        return render(request,'forminfo.html', {'email': email, 'password': password})
    
    else:
        return render (request,'forminfo.html')
