from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout,authenticate
from django.contrib import messages
from django.conf import settings
from .models import file,feedback
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    username = request.user.username
    return render(request,'home.html',{'username':username})


def logincheck(request):
    if request.method=='POST':
        username_=request.POST['username']
        password_=request.POST['password']
        user=authenticate(request,username=username_,password=password_)
        if user is not None:
            params={'username':username_}
            login(request,user)
            messages.success(request,'succesfully loged in')
            print(params)
            return render(request,'home.html',params)
        else:
            messages.error(request,'invalid cradentials')
            return render(request,'home.html')
    return HttpResponse("Error 404 not avalable")




def logoutcheck(request):
    
    logout(request)
    messages.success(request,'succesfully loged out')
    username = request.user.username
    return redirect('/',{'username':username})
     

@login_required(login_url='/login')
def viewfile(request):
    post=file.objects.all()
    username = request.user.username
    context={
        "post":post,
        'username':username
    }
    return render(request,"fileshow.html",context)



@login_required(login_url='/login')
def sub1(request):
    post=file.objects.filter(subject__icontains='math')
    username = request.user.username
    context={
        "post":post,
        'username':username
    }
    return render(request,'fileshow.html',context)


@login_required(login_url='/login')
def sub2(request):
    post=file.objects.filter(subject__icontains='physics')
    username = request.user.username
    context={
        "post":post,
        'username':username
    }
    return render(request,'fileshow.html',context)


@login_required(login_url='/login')
def sub3(request):
    post=file.objects.filter(subject__icontains='chemistry')
    username = request.user.username
    context={
        "post":post,
        'username':username
    }
    return render(request,'fileshow.html',context)


@login_required(login_url='/login')
def sub4(request):
    post=file.objects.filter(subject__icontains='mechanical')
    username = request.user.username
    context={
        "post":post,
        'username':username
    }
    return render(request,'fileshow.html',context)



@login_required(login_url='/login')
def sub5(request):
    post=file.objects.filter(subject__icontains='workshop')
    username = request.user.username
    context={
        "post":post,
        'username':username
    }
    return render(request,'fileshow.html',context)


@login_required(login_url='/login')
def feed(request):
    
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        issue=request.POST['issue']
        if len(name)<2 or len(email)<3 or len(issue)<2 :
            messages.error(request, 'Please fill the form correctly')
        else:
            messages.success(request, 'your form is succesfully submited')

            Contact=feedback(name=name,email=email,issue=issue)
            Contact.save()

    username = request.user.username
    return render(request,'feedback.html',{'username':username})

    

@login_required(login_url='/login')
def search(request):
    if request.method=='GET':
        one=request.GET['query']
        post= file.objects.filter(name__icontains=one)
        
        username = request.user.username
        params={'post': post,'username':username}
        return render(request, 'search.html', params)
    return render(request, 'home.html', {"username":username})
