from django.shortcuts import render
from .models import Emp
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
def home(request):
    data=Emp.objects.all()
    return render(request,'index.html',{'data':data})
def addemp(request):
    name=request.POST['name']
    sal=request.POST['sal']
    sal=int(sal)
    address=request.POST['address']
    e=Emp()
    e.name=name
    e.sal=sal
    e.address=address
    e.save()
    data=Emp.objects.all()
    return render(request,'index.html',{'data':data})
def delete(request):
    return render(request,'delete.html')
def delt(request):
    eid=request.GET['eid']
    Emp.objects.get(id=eid).delete()
    data=Emp.objects.all()
    return render(request,'index.html',{'data':data})
def search(request):
    eid=request.POST['eid']
    e=Emp.objects.get(id=eid)
    return render(request,'index.html',{'data':[e]})
def update(request):
    e=Emp()
    e.id=request.POST['eid']
    e.name=request.POST['name']
    sal=request.POST['sal']
    e.sal=int(sal)
    e.address=request.POST['address']
    e.save()
    data=Emp.objects.all()
    return render(request,'index.html',{'data':data})
def uregs(request):
    if request.method=='POST':
        uname=request.POST['uname']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pwd=request.POST['pwd']
        user=User.objects.create_user(username=uname,password=pwd,email=email,first_name=fname,last_name=lname)
        user.save()
        messages.success(request,'sucessfully registerd')
        return render(request,'ulogin.html')
    else:
        return render(request,'uregs.html')
def ulogin(request):
    if request.method=='POST':
        uname=request.POST['uname']
        pwd=request.POST['pwd']
        user=auth.authenticate(username=uname,password=pwd)
        if user is not None:
            auth.login(request,user)
            return render(request,'uhome.html')
        else:
            messages.info(request,'Invalid userid and password')
            return render(request,'ulogin.html')
    else:
        return render(request,'ulogin.html')
def ulogout(request):
    auth.logout(request)
    messages.info(request,'sucessfully logout')
    return render(request,'ulogin.html')