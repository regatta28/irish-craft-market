from django.shortcuts import render, get_object_or_404, redirect
<<<<<<< HEAD
from .models import Product
=======
from products.models import Product
>>>>>>> d9b3d8c3550826e6b99d736146926b7aa5748717
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import ProductPostForm


def all_products(request):
    products = Product.objects.all().order_by('-created_date')
    return render(request, 'products.html', {'products': products})
    
def productdetails(request, id):
    """
    Create a view that return a single
    Post object based on the post ID and
    and render it to the 'postdetail.html'
    template. Or return a 404 error if the
    post is not found
    """
    product = get_object_or_404(Product, pk=id)
    product.views += 1
    product.save()
    return render(request, "productdetails.html", {'product': product})

@login_required(login_url="/user/login?next=products/new")
def new_product(request):
    if request.method == "POST":
        form = ProductPostForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.advertiser = request.user
            product.save()
            return redirect(productdetails, product.pk)
    else:
        form = ProductPostForm()
    return render(request, 'productform.html', {'form': form})

@login_required(login_url="/user/login?next=products/edit/")
def edit_product(request, id):
   product = get_object_or_404(Product, pk=id)
   if request.method == "POST":
       form = ProductPostForm(request.POST, request.FILES, instance=product)
       if form.is_valid():
           product = form.save(commit=False)
           product.advertiser = request.user
           product.save()
           return redirect(productdetails, product.pk)
   else:
       form = ProductPostForm(instance=product)
       return render(request, 'productform.html', {'form': form})
    
    
    
    




