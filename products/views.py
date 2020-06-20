from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product

# Create your views here.
def home(req):
    products = Product.objects
    return render(req,'products\home.html',{'products':products})

@login_required
def create(req):
    if(req.method == 'POST'):
        product = Product()
        product.title = req.POST['title']
        product.body = req.POST['body']
        product.image = req.FILES['image']
        product.icon =req.FILES['icon']
        if(req.POST['url'].startswith('http://') or req.POST['url'].startswith('https://')):
            product.url = req.POST['url']
        else:
            product.url = 'http://'+req.POST['url']
        product.hunter = req.user
        product.save()
        return redirect('/products/' + str(product.id))

    else:    
        return render(req,'products\create.html')


def product(req,id):
    product = get_object_or_404(Product,pk=id)
    print(product)
    return render(req,'products\detail.html',{'product':product})

@login_required
def upvote(req,id):
    if(req.method=='POST'):
        product = get_object_or_404(Product,pk=id)
        product.votes_total += 1
        product.save()
        return redirect('/products/' + str(product.id))
