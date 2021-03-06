from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Product,ProQuantity,Transaction
from .forms import List,Quentity
from datetime import date
# Create your views here.

def index(request):
    if request.method=="POST":
            model= List(request.POST,request.FILES)  
            if model.is_valid():
                    model.save()
            return redirect(product)
    else:
           model = List()  
    return render(request,'blog/index.html',{'form':model})
  

    

@login_required(login_url='login')
def product(request):
     pro = Product.objects.all()
     params  = {'products':pro}
     return render(request,'blog/product.html',params)




def signup(request):
        if request.method == "POST":
                username = request.POST['username']
                email = request.POST['email']
                password = request.POST['password']
                fname = request.POST['fname']
                lname = request.POST['lname']
                user = User.objects.create_user(username,email,password)
                user.first_name = fname
                user.last_name = lname
                user.save()
                messages.success(request,"Your account has been successfully created")
                return redirect(index)
        else:
                print("not Posted")      
        return render(request,"blog/signup.html")



def handlelogin(request):
        if request.method == "POST":
                loginusername = request.POST['username']
                loginpassword = request.POST['pass']
                user = authenticate(username=loginusername, password=loginpassword)
                if user is not None:
                        login(request,user)
                        messages.success(request,"Login successfully")  
                        return redirect(product)
                else:
                        messages.error(request,"invalid login username and password")    
                        return redirect(index)    
        return render(request,"blog/login.html")



@login_required(login_url='login')
def handlelogout(request):
        logout(request)
        messages.success(request,"Logout successfully") 
        return redirect(index)    


@login_required(login_url='login')
def order(request):   
        products=Transaction.objects.filter(userId=request.user.id, status="buy").select_related()
        param  = {'model':products}
        return render(request,'blog/order.html',param)






@login_required(login_url='login')
def viewitems(request,itemid):
        items = Product.objects.get(id=itemid)
        model = ProQuantity.objects.all()  
        params  = {'item':items,'model':model}
        return render(request,'blog/product_items.html',params)



@login_required(login_url='login')
def buycate(request):      
        
        if request.method=="POST":
                useridget = User.objects.get(id=request.user.id)
                product_id = Product.objects.get(id=request.POST['id'])
                quantity = ProQuantity.objects.get(id=request.POST['quantityID'])

                if 'buynow' in request.POST:                      
                        cart_item = Transaction.objects.create(userId=useridget ,productid=product_id, quantityid=quantity, status="Buy")
                        messages.success(request,"Transaction has been done successfully") 
                        return redirect(viewitems,request.user.id)

                elif 'addtocart' in  request.POST:
                        cart_item = Transaction.objects.create(userId=useridget ,productid=product_id, quantityid=quantity, status="AddToCart")
                        messages.success(request,"Your item  has been add to cart successfully") 
                        return redirect(cart)
                else:
                        cart_item = Transaction.objects.create(userId=useridget, productid=product_id,quantityid=quantity,status="AddToWishList")
                        messages.success(request,"Your item  has been add to wish list successfully") 
                        return redirect(wishlist)
        else:
                model = ProQuantity.objects.all()  
        return render(request,'blog/index.html',{'model':model,})


@login_required(login_url='login')
def wishlist(request):
        products=Transaction.objects.filter(userId=request.user.id, status="AddToWishList").select_related()
        param = {'model': products}
        return render(request, 'blog/whishlist.html', param)


@login_required(login_url='login')
def delete(request,itemsid):
        productsdelete=Transaction.objects.filter(id=itemsid).update(status="delete")
        messages.success(request, "Your item  has been delete successfully")
        return redirect(wishlist)

     
@login_required(login_url='login')
def cart(request):
        products = Transaction.objects.filter(userId=request.user.id,status="AddToCart").select_related()
        itemsCount = Transaction.objects.filter(userId=request.user.id, status="AddToCart").count()
        request.session['countitems'] = itemsCount
        totalPrice = 0
        for item in products:
                totalPrice += item.productid.price

        param = {'model': products, 'itemCount': itemsCount,'totalPrice':totalPrice}
        return render(request, 'blog/cart.html', param)


@login_required(login_url='login')
def cartparam(request,itemsid):
        productsCancel=Transaction.objects.filter(id=itemsid).update(status="AddToCart")
        messages.success(request, "Your item  has been add to cart successfully")
        return redirect(cart)


@login_required(login_url='login')
def cancel(request, itemsid):

        cancelorder = Transaction.objects.filter(id=itemsid).update(status="Cancel")
        messages.success(request,"Your item  has been cancel successfully") 
        return redirect(order)
                

@login_required(login_url='login')
def canceltotal(request):
        productsCancel=Transaction.objects.filter(userId=request.user.id, status="Cancel").select_related()
        param = {'model': productsCancel}
        return render(request, 'blog/canceltotal.html', param)


@login_required(login_url='login')
def processtobuy(request):
        products = Transaction.objects.filter(userId=request.user.id,status="AddToCart").count()
        for x in range(products):
                products = Transaction.objects.filter(userId=request.user.id,status="AddToCart").update(status="Buy")      
        messages.success(request, "Your item  has been order successfully")                  
        return redirect(order)
