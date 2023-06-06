
from datetime import date
from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout

from .models import Item
from datetime import datetime


# signup
def signup(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, "Account Created Successfully!!")
            fm.save()
    else:
        fm = SignUpForm()
    return render(request, "accounts/signup.html", {"form": fm})


# Login View
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data["username"]
                upass = fm.cleaned_data["password"]
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Logged in Successfully")
                    return HttpResponseRedirect("/index/")
        else:
            fm = AuthenticationForm()
        return render(request, "accounts/userlogin.html", {"form": fm})
    else:
        return HttpResponseRedirect("/index/")


# Logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/index/")

    

def index(request):
    if request.user.is_authenticated:
        return render(request, "accounts/index.html")
    else:
        return HttpResponseRedirect("/")


def lost_items(request):
    if request.user.is_authenticated:
        return render(request, "accounts/lost.html")
    else:
        return HttpResponseRedirect("/")

def found_items(request):
    if request.user.is_authenticated:
        return render(request, "accounts/found.html")
    else:
        return HttpResponseRedirect("/")


def claim(request):
    if request.user.is_authenticated:
        return render(request, "accounts/index.html")
    else:
        return HttpResponseRedirect("/")


def faq(request):
    if request.user.is_authenticated:
        return render(request, "accounts/index.html")
    else:
        return HttpResponseRedirect("/")
    
def contact(request):
    if request.user.is_authenticated:
        return render(request, "accounts/index.html")
    else:
        return HttpResponseRedirect("/")
    
def success(request):
    if request.user.is_authenticated:
        return render(request, "accounts/success.html")
    else:
        return HttpResponseRedirect("/")



from .forms import LostItemForm, FoundItemForm




def report_found_items(request):
    if request.method == 'POST':
        item_name=request.POST["item_name"]
        item_description=request.POST["item_description"]
        date=request.POST["date"]
        location=request.POST["location"]
        contact=request.POST["contact"]
        image=request.FILES.get("image")

        fd = Item(
            title= item_name,
            description = item_description,
            contact_email= contact,
            date_lost_or_found =date,

            location=location,
            owner= request.user,
            image= image,
            is_found= True
        ) 
        fd.save()
        return redirect('success')
    else:
        return render(request, "accounts/found.html")








def report_lost_items(request):
    if request.method == 'POST':
        item_name=request.POST["item_name"]
        item_description=request.POST["item_description"]
        date=request.POST["date"]
        location=request.POST["location"]
        contact=request.POST["contact"]
        

        fd = Item(
            title= item_name,
            description = item_description,
            contact_email= contact,
            date_lost_or_found =date,

            location=location,
            owner= request.user,
            
            
        ) 
        fd.save()
        return redirect('success')
    

    return render(request, "accounts/lost.html")





