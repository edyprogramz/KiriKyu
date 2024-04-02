from django.shortcuts import render, redirect, get_object_or_404
from item.models import Item
from django.http import JsonResponse

# Create your views here.
# def checkout(request):
    
#     if request.method == 'POST' and request.is_ajax():
#         total_amount = request.POST.get('total_amount')
        
#         # Process the total amount as needed
        
#         # For demonstration, let's just return the total amount back
#         return JsonResponse({'total_amount': total_amount})
#     else:
#         return JsonResponse({'error': 'Invalid request'})
    
    



def add_to_cart(request, item_id):
    item = Item.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity', 1))
    if quantity <= 0:
        # Invalid quantity, redirect back to item detail page
        return redirect('item:detail', item_id=item_id)
    
    # Add item to the cart with specified quantity
    request.session.setdefault('cart', {})
    request.session['cart'][item_id] = request.session['cart'].get(item_id, 0) + quantity
    request.session.modified = True
    
    return redirect('cart:view_cart')

def remove_from_cart(request, item_id):
    if request.method == 'POST':
        if 'cart' in request.session and str(item_id) in request.session['cart']:
            del request.session['cart'][str(item_id)]
            request.session.modified = True
    return redirect('cart:view_cart')

def view_cart(request):
    cart_items = []
    total_price = 0
        

    if 'cart' in request.session:
        for item_id, quantity in request.session['cart'].items():
            item = Item.objects.get(pk=item_id)
            total_price += item.price * quantity
            cart_items.append({'item': item, 'quantity': quantity})

    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

def checkout(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, "checkout.html", {
        'item':item
    })
