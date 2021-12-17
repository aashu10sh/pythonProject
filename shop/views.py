from django.shortcuts import render, redirect
from .models import Student
# Create your views here.
from .models import Shop, Product, Deal
from shop.forms import ProductForm


# Create your views here.
def index(req):
    shops = Shop.objects.all()
    products = Product.objects.all()
    deals = Deal.objects.all()
    context = {
        "shops" : shops,
        "products" : products,
        "deals" : deals
    }
    return render(req, "shop/index.html", context)


def product_list(request): 
    product_list = Product.objects.all()
    context ={
        'products':product_list
    }
    return render(request, 'shop/showproducts.html',context)

def shop_list(request):

    shop_list = Shop.objects.all()
    context = {
        'shop':shop_list
    }
    return render(request,'shop/showshop.html',context)

def main(request):
    return render(request,'shop/main.html')

def deal_list(request):
    deals = Deal.objects.all()
    context = {
        'deals':deals
    }
    return render(request,'shop/showdeals.html',context)

def product_form(request):
    return render(request,'shop/product_view.html')


def product(request, id, name):
    return render(request, "shop/product.html",{"id":id,"name":name})


def user(request):
    agent = request.headers['User-Agent']
    return render(request, "shop/usera.html",{"usera":agent})
    # return {'usera':}


def product_data(request):
    username = request.POST['name']
    rollnumber = request.POST['rollnumber']
    student_data = Student.objects.create(username=username,roll=rollnumber)
    student_data.save()

    return render(request, "shop/product_data.html",{"username":"SAVED"})

def product(request):
    if request.method.lower() == "post":
        form = ProductForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/productshow')
            except Exception as e:
                print(e)
                pass
    else:
        form = ProductForm()
        return render(request, "shop/product_new.html",{"form":form})



def productshow(request):
    products = Product.objects.all()
    return render(request, "shop/product_list.html",{"products":products})


def productedit(request, id):
    product = Product.objects.get(id=id)
    return render(request, "shop/product_edit.html",{"product":product})

    # form = ProductForm(request.POST, instace=product)
    # print(form)
    # if form.is_valid():
    #     form.save()
    #     return redirect('/productshow')
    # return redirect



def productupdate(request, id):
    product = Product.objects.get(id=id)
    form = ProductForm(request.POST, instance=product)
    print(form)
    if form.is_valid():
        form.save()
        return redirect('/productshow')
    return render(request, "shop/product_edit.html",{"product":product})



def productdestroy(request):
    return None