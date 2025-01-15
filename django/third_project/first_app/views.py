from django.shortcuts import render

# Create your views here.
def details(request):
    return render (request,'./first_app/index.html', {'Courses':[
        {'course':'Python', 'price':100},
        {'course':'Java', 'price':200},
        {'course':'C++', 'price':300},
        {'course':'C#', 'price':400},
        
    ]},
                   
                   #this is for if else condition. This line are transfering data
                   #from views to html template or backend to frontend
                # context={'Student':'Anis', 'Roll':'112063', 'Sec':'B', 'Age':10},
                   )