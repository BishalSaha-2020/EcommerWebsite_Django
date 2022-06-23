from django.shortcuts import render
from django.http import HttpResponse
from . models import Items
from math import ceil
from .models import Items, Contact

def index(request):
    products= Items.objects.all()
    allProds=[]
    catprods= Items.objects.values('category', 'id')
    cats= {item["category"] for item in catprods}
    for cat in cats:
        prod=Items.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params={'allProds':allProds }
    return render(request,"shop/index.html", params)

    return render(request,"shop/index.html", params)

def about(request):
    return render(request,"shop/about.html")

def contact(request):

    if request.method == "POST":
        print(request)
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        print(name, email, phone, desc)
    return render(request,"shop/contact.html")



def tracker(request):
    return HttpResponse("We are at tracker")

def search(request):
    return HttpResponse("We are at search")

def productView(request, myid):
    product=Items.objects.filter(id=myid)
    print(product)
    return render(request, "shop/prodView.html", {'product':product[0]})

def checkout(request):
    return HttpResponse("We are at checkout")