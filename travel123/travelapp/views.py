from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Resort


# Create your views here.
def fun(request):
    obj=Place.objects.all()
    obj1=Resort.objects.all()
    return render(request,'index.html',{'result':obj,'result1':obj1})






















# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res1=x+y
#     res2=x-y
#     res3=x*y
#     res4=x/y
#     return render(request,'result.html',{'obj1':res1,'obj2':res2,'obj3':res3,'obj4':res4})

