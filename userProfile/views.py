from django.shortcuts import render, redirect
from products.models import *
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
# Create your views here.


def profile(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user)
        currentUser = Profile.objects.get(user=user)
        products = Product.objects.filter(publisher=user)
        context = {
            "products": products.order_by("-order_key"),
            "currentUser": currentUser,
        }
        return render(request, "profile.html", context)
    else:
        return redirect("UserProfile:signin")

def editProfile(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user)
        currentUser = Profile.objects.get(user=user)
        products = Product.objects.filter(publisher=user)

        userForm = UpdateUserForm(instance=request.user)
        profile = Profile.objects.get(user=user)
        profileForm = UpdateProfileForm(instance=profile)

        context = {
            "products": products.order_by("-order_key"),
            "currentUser": currentUser,
            "profileForm": profileForm,
            "userForm": userForm,
        }
        return render(request, "editProfile.html", context)
    else:
        return redirect("UserProfile:signin")



def editValue(request):
    update(request)
    return redirect("/accounts/profile")

def update(request,Update=True):
    if ( not request.user.is_authenticated and not Update )or (request.user.is_authenticated and Update):
        if request.method == "POST":
            if Update:
                user = request.user
            else:
                user = User.objects.get(username=request.POST['username'])  
            
            userForm = UpdateUserForm(request.POST, instance=user)
            profile = Profile.objects.get(user=user)
            print(profile)
            profileForm = UpdateProfileForm(request.POST, request.FILES, instance=profile)

            if userForm.is_valid and profileForm.is_valid:
                userForm.save()
                profileForm.save()
    else:
        return redirect("UserProfile:signin")

def signUp(request):
    userForm = CreateUserForm()
    profileForm = UpdateProfileForm()
    context = {
        "profileForm": profileForm,
        "userForm": userForm,
    }
    return render(request, "signUp.html", context)

def addAccount(request):
    if request.method == "POST":
        post = request.POST
        username= post['username']
        password= post['password']
        first_name= post['first_name']
        last_name= post['last_name']
        if not User.objects.filter(username=username):
            User.objects.create_user(
                username = username,
                password = password,
                first_name = first_name,
                last_name = last_name,
            )
            update(request,False)
    return redirect("/accounts/signin")

def signin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            post = request.POST
            username = post['username']
            password = post['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    return redirect("/")
                else:
                    return redirect("/accounts/signin")
            else:
                return redirect("/accounts/signin")
            
        else:
            if request.user.is_authenticated:
                user = User.objects.get(username=request.user)
                currentUser = Profile.objects.get(user=user)
            else:
                currentUser = None
            context = {
                "currentUser": currentUser,
            }
            return render(request, "signin.html", context)
    else:
        return redirect("/")

def logout(request):
    auth.logout(request)
    return redirect("Products:index")