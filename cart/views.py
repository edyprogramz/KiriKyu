from django.shortcuts import render, redirect, get_object_or_404
from item.models import Item
from .models import CartItem

from core.models import PaymentMethod
from django.http import JsonResponse

# Create your views here.
# def add_to_cart(request, item_id):
#     item = Item.objects.get(pk=item_id)
#     quantity = int(request.POST.get('quantity', 1))
#     if quantity <= 0:
#         # Invalid quantity, redirect back to item detail page
#         return redirect('item:detail', item_id=item_id)
    
#     # Add item to the cart with specified quantity
#     request.session.setdefault('cart', {})
#     request.session['cart'][item_id] = request.session['cart'].get(item_id, 0) + quantity
#     request.session.modified = True
    
#     return redirect('cart:view_cart')

# def remove_from_cart(request, item_id):
#     if request.method == 'POST':
#         if 'cart' in request.session and str(item_id) in request.session['cart']:
#             del request.session['cart'][str(item_id)]
#             request.session.modified = True
#     return redirect('cart:view_cart')

# def view_cart(request):
#     cart_items = []
#     total_price = 0
        

#     if 'cart' in request.session:
#         for item_id, quantity in request.session['cart'].items():
#             item = Item.objects.get(pk=item_id)
#             total_price += item.price * quantity
#             cart_items.append({'item': item, 'quantity': quantity})

#     return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

def checkout(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    payment_method = PaymentMethod.objects.filter(user=item.created_by)

    return render(request, "checkout.html", {
        'item':item,
        "payment_method":payment_method,
    })

def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(cart_item.item.price * cart_item.quantity for cart_item in cart_items)

    return render(request, "cartt.html", {
        "cart_items":cart_items,
        "total_price":total_price
    })


def add_to_cart(request, item_id):
    item = Item.objects.get(pk=item_id)
    
    # Check if the item is already in the user's cart
    cart_item, created = CartItem.objects.get_or_create(user=request.user, item=item)
    
    # If the item is already in the cart, increase its quantity
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect('cart:view_cart')


def remove_from_cart(request, item_id):
    # Retrieve the item to remove from the cart
    item = Item.objects.get(pk=item_id)
    
    # Retrieve the cart item
    cart_item = CartItem.objects.get(user=request.user, item=item)
    
    # If the quantity is more than 1, decrease it; otherwise, remove the cart item
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    
    return redirect('cart:view_cart')
