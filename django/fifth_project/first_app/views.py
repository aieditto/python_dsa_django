from django.shortcuts import render

# Create your views here.
def contact(request):
        return render(request,'first.html')

def form(request):
    if request.method == 'POST':
        print(request.POST)
        email=request.POST.get('email')
        password=request.POST.get('password')
        select=request.POST.get('select')
        return render(request,'forminfo.html', {'email': email, 'password': password, 'select':select})
    
    else:
        return render (request,'forminfo.html')


