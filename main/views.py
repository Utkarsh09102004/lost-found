from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import LostForm, FoundForm, userRegistration
from .models import *
from .image_matching import image_matcher





def home(request):


    return render(request,'main.html')

def loginPage(request):

    if request.method == 'POST':
        username= request.POST.get('username')
        password = request.POST.get("password")
        user=authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, "No user found")



    context={}
    return render(request, 'main/login.html', context)


def home(request):

    username = request.user.username

    context={'name':username}
    return render(request, 'main/home.html', context)

def registration(request):
    form= userRegistration()
    if request.method == 'POST':
        form= userRegistration(request.POST)
        if form.is_valid():
            form.save()
        
        return redirect('login')
    context={'form':form}
    return render(request,'main/register.html',context)
    

def loser(request):
    initial_data = {
        'loser': request.user.username,
    }

    if request.method == 'POST':
        form = LostForm(request.POST, request.FILES, initial=initial_data)

        if form.is_valid():
            lost_item = form.save(commit=False)
            lost_item.loser = request.user
            lost_item.save()
            return redirect('home')
    else:
        form = LostForm(initial=initial_data)

    context = {'form': form}
    return render(request, 'main/loser.html', context)



def founder(request):
    initial_data = {
        'loser': request.user.username,
    }

    if request.method == 'POST':
        form = FoundForm(request.POST, request.FILES, initial=initial_data)

        if form.is_valid():
            Found_item = form.save(commit=False)
            Found_item.founder = request.user
            Found_item.save()
            return redirect('home')
    else:
        form = FoundForm(initial=initial_data)

    context = {'form': form}
    return render(request, 'main/founder.html', context)


def status(request):
    lostitems=LostItem.objects.all()


    context={'lost': lostitems }
    return render(request,'main/status.html',context)

def item(request,pk):
    item=LostItem.objects.get(id=pk)

    # if request.method == 'POST':
    #     results=image_matcher(item.image.path)
    #     print(results)
    #     print()
    #     request.session['result'] = results

    context={ 'item': item }
    return render(request,'main/item.html',context)

def matched(request,pk):
    item=LostItem.objects.get(id=pk)
    results=image_matcher(item.image.path)
    # filtered_lists = request.session.get('result')
    filtered_list = FoundItem.objects.filter(id__in=[item for item in results])
    context={ 'lost': filtered_list}
    return render(request,'main/matched.html',context)


def contact(request,pk):
    user=CustomUser.objects.get(id=pk)
    context={'user':user}
    return render(request,'main/contact.html',context)


