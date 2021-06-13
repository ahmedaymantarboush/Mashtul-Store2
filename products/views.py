from django.shortcuts import render, redirect
from .models import *
from userProfile.models import *
from comments.models import *
from django.contrib.auth.models import User
from django.contrib import messages
import math
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user)
        userProfile = Profile.objects.get(user=user)
        if request.method == "POST":
            product = Product.objects.get(id=request.POST["id"])
            if "love" in request.POST:
                if product in userProfile.wishes.all():
                    userProfile.wishes.remove(product)
                elif not product in userProfile.wishes.all():
                    userProfile.wishes.add(product)
            elif "buy" in request.POST:
                if product in userProfile.cart.all():
                    userProfile.cart.remove(product)
                elif not product in userProfile.cart.all():
                    userProfile.cart.add(product)
        currentUser = Profile.objects.get(user = user)
    else:
        currentUser = None
    products = Product.objects.all()
    if 'search' in request.GET:
        if request.GET['search']:
            if Product.objects.filter(name__icontains=request.GET['search']).exists():
                products = Product.objects.filter(name__icontains=request.GET['search'])
            else:
                products = Product.objects.filter(name__icontains=request.GET['search'])
        else:
            products = Product.objects.all()
    else:
        products = Product.objects.all()
    context = {
        "products": products.order_by("-order_key"),
        "currentUser": currentUser,
    }
    return render(request, "index.html" , context)

def productDetails(request,productId):
    if request.user.is_authenticated:
        product = Product.objects.get(id=productId)
        comments = Comment.objects.filter(product=product)
        print(product.image.url)
        if product.sale:
            price = product.price * ( 100.0 - product.sale )
        else:
            price = 0
        available = product.quantity - product.sold
        if not product.raters.count() == 0:
            rate = product.rate / product.raters.count()
        else:
            rate = 0
        currentUser = Profile.objects.get(user = request.user)
        context = {
            "product": product,
            "price": price,
            "available": available,
            "rate": rate,
            "currentUser": currentUser,
            "productDetail": True,
            "comments":comments
        }
        return render(request,"productDetails.html" , context)
    else:
        return redirect("UserProfile:signin")

def addProduct(request):
    if request.user.is_authenticated:
        currentUser = Profile.objects.get(user = request.user)
        Units = Unit.objects.all()
        Categories = Category.objects.all()
        context = {
            "currentUser": currentUser,
            "Units":Units,
            "Categories": Categories,
        }
        return render(request,"addProduct.html" , context)
    else:
        return redirect("UserProfile:signin")


def cart(request):
    products = None
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user)
        userProfile = Profile.objects.get(user=user)
        if request.method == "POST":
            product = Product.objects.get(id=request.POST["id"])
            if "love" in request.POST:
                if product in userProfile.wishes.all():
                    userProfile.wishes.remove(product)
                elif not product in userProfile.wishes.all():
                    userProfile.wishes.add(product)
            elif "buy" in request.POST:
                if product in userProfile.cart.all():
                    userProfile.cart.remove(product)
                elif not product in userProfile.cart.all():
                    userProfile.cart.add(product)
        currentUser = Profile.objects.get(user = user)
        products = currentUser.cart.all
        context = {
            "product": products.order_by("id"),
            "currentUser": currentUser,
        }
        return render(request,"index.html" , context)
    else:
        return redirect("UserProfile:signin")
def wishes(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user)
        userProfile = Profile.objects.get(user=user)
        if request.method == "POST":
            product = Product.objects.get(id=request.POST["id"])
            if "love" in request.POST:
                if product in userProfile.wishes.all():
                    userProfile.wishes.remove(product)
                elif not product in userProfile.wishes.all():
                    userProfile.wishes.add(product)
            elif "buy" in request.POST:
                if product in userProfile.cart.all():
                    userProfile.cart.remove(product)
                elif not product in userProfile.cart.all():
                    userProfile.cart.add(product)
        currentUser = Profile.objects.get(user = user)
        products = currentUser.wishes.all
        context = {
            "products":products.order_by("-order_key"),
            "currentUser": currentUser,
        }
        return render(request,"index.html" , context)
    else:
        return redirect("UserProfile:signin")

def myProducts(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user)
        currentUser = Profile.objects.get(user = user)
        products = Product.objects.filter(publisher = user)
        context = {
            "products": products.order_by("-order_key"),
            "currentUser": currentUser,
        }
        return render(request,"index.html" , context)
    else:
        return redirect("UserProfile:signin")

def add(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            p=request.POST
            productName = p["productName"]
            price = float(p["price"])
            sale=float(p["sale"])
            unit = Unit.objects.get(id = p["unit"])
            category= Category.objects.get(id = p['category'])
            quantity = float(p["quantity"])
            description = p["description"]
            image = request.FILES.get('id_image') or 'Products/default.jpg'
            pro = Product(
                order_key=int(Product.objects.all().count()) + 10000,
                name=productName,
                price=price,
                quantity=quantity,
                sale=sale,
                unit=unit,
                description=description,
                publisher=request.user,
                category=category,
                image=image
                )
            pro.save()
        return redirect("Products:index")
    else:
        return redirect("UserProfile:signin")

def action(request,productId):
    if request.user.is_authenticated:
        if request.method=='POST':
            p = request.POST
            product=Product.objects.get(id = productId)
            if 'buy' in p:
                pass
            elif 'addToCart' in p:
                if product in userProfile.cart.all():
                    userProfile.cart.remove(product)
                elif not product in userProfile.cart.all():
                    userProfile.cart.add(product)
            elif 'love' in p:
                    if product in userProfile.wishes.all():
                        userProfile.wishes.remove(product)
                    elif not product in userProfile.wishes.all():
                        userProfile.wishes.add(product)
        return redirect('products:productDetails', productId)
    else:
        return redirect("UserProfile:signin")
