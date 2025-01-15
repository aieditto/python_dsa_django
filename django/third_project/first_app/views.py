from django.shortcuts import render

# Create your views here.
def details(request):
    return render (request,'./first_app/index.html', context=
                   {'Student':'Anis', 'Roll':'112063', 'Sec':'B', 'Age':10},
                   )