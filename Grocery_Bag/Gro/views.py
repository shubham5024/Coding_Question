from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import *
from django.http import HttpResponse,JsonResponse
# Create your views here.
def index(request):
    return render(request,'index.html')
def add_item(request):
    return render(request,'add_item.html')

def update_item(request):
    return render(request,'update_item.html')


# def add_submit(request):
#     if request.method=="POST":
#         if request.POST.get("title") and
def add_submit(request):
    obj=grocery()
    obj.iname = request.GET['iname']
    obj.quant = request.GET['quant']
    obj.status = request.GET['status']
    obj.date=request.GET['date']
    obj.save()
    mydictionary = {
        "alltodos" :grocery.objects.all()
    }
    print(grocery.objects.all())
    return render(request,'add_item.html',context=mydictionary)

def view_list(request):
    mydictionary={
        "alltodos":grocery.objects.all()
    }
    print(grocery.objects.all())
    return render(request,'view_list.html',context=mydictionary)