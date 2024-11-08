from django.shortcuts import render
from django.http import HttpResponse


def Welcome(request):  
    # return HttpResponse('<h1> Hello world</h1>')
    return render(request,'index.html')

def User(request):
    username=request.GET['username']
    print(username)
    return render(request,'user.html',{'name':username})