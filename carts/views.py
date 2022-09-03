from http.client import HTTPResponse
from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Product, Variation
from .models import Cart, CartItem
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


# def add_cart(request, product_id):
#     # current_user = request.user
#     product = Product.objects.get(id=product_id) # get the product
#     try: 
#         cart = Cart.objects.get(cart_id=_cart_id(request)) # get the cart using the cart_id present in the session
#     except Cart.DoesNotExist:
#         cart = Cart.objects.create(
#             cart_id = _cart_id(request)
#         )
#     cart.save()
    
#     try:
#         cart_item = CartItem.objects.get(product=product, cart=cart)
#         cart_item.quantity += 1 # cart_item.quantity = cart_item.quantity + 1
#         cart_item.save()
#     except CartItem.DoesNotExist:
#         cart_item = CartItem.objects.create(
#             product = product,
#             quantity = 1,
#             cart = cart,            
#         )
#         cart_item.save()
#     # return HttpResponse(cart_item.product)
#     # exit()
#     return redirect('cart')



def add_cart(request, product_id):
    if request.method == 'POST':
        for item in request.POST:
            key = item
            value = request.POST[key]
            
            try:
                variation = Variation.objects.get(variation_category__iexact=key, variation_value__iexact=value)
                print(variation)
            except:
                pass          
    
    product = Product.objects.get(id=product_id) # get the product
    try: 
        cart = Cart.objects.get(cart_id=_cart_id(request)) # get the cart using the cart_id present in the session
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
    cart.save()
    
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1 # cart_item.quantity = cart_item.quantity + 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product = product,
            quantity = 1,
            cart = cart,            
        )
        cart_item.save()
    # return HttpResponse(cart_item.product)
    # exit()
    return redirect('cart')
    
    # current_user = request.user
    # product = Product.objects.get(id=product_id) # get the product
    # if current_user.is_authenticated:
    #     if request.method == 'POST':
    #         for item in request.POST:
    #             key = item
    #             value = request.POST[key]
                
    #     is_cart_item_exists = CartItem.objects.filter(product= product, user=current_user).exists()
    #     if is_cart_item_exists:
    #         id = []
            
    #         for item in cart_item:
    #             id.append(item.id)
                
    # try: 
    #     cart = Cart.objects.get(cart_id=_cart_id(request)) # get the cart using the cart_id present in the session
    # except Cart.DoesNotExist:
    #     cart = Cart.objects.create(
    #         cart_id = _cart_id(request)
    #     )
    # cart.save()
    
    # try:
    #     cart_item = CartItem.objects.get(product=product, cart=cart)
    #     cart_item.quantity += 1 # cart_item.quantity = cart_item.quantity + 1
    #     cart_item.save()
    # except CartItem.DoesNotExist:
    #     cart_item = CartItem.objects.create(
    #         product = product,
    #         quantity = 1,
    #         cart = cart,            
    #     )
    #     cart_item.save()
    # # return HttpResponse(cart_item.product)
    # # exit()
    # return redirect('cart')

def remove_cart(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')

def remove_cart_item(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cart')
    

# Create your views here.
def cart(request, total=0, quantity=0, cart_items=None):
    try:
        tax = 0
        grand_total = 0
        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(user=request.user, is_active=True)
        else:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.discounted_price * cart_item.quantity)
            quantity += cart_item.quantity
        # tax = (2 * total)/100
        grand_total = total
    except ObjectDoesNotExist:
        pass # just ignore
    
    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        # 'tax': tax,
        'grand_total': grand_total,
        
    }
    
    return render(request, 'shop/cart.html', context)

@login_required(login_url='login')
def checkout(request, total=0, quantity=0, cart_items=None):
    try:
        tax = 0
        grand_total = 0
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.discounted_price * cart_item.quantity)
            quantity += cart_item.quantity
        # tax = (2 * total)/100
        grand_total = total
    except ObjectDoesNotExist:
        pass # just ignore
    
    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        # 'tax': tax,
        'grand_total': grand_total,
        
    }
    return render(request, 'shop/checkout.html', context)