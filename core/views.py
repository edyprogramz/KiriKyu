from django.shortcuts import render, redirect

from .forms import SignupForm
from item.models import Item, Category
from .models import PaymentMethod
# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)[0:10]
    categories = Category.objects.all()[:7]
    latest_items = Item.objects.order_by('-created_on')[:5]
        
    
    return render(request, "core/index.html", {
        "items": items,
        "categories": categories,
        "latest_items": latest_items
    })

def contact(request):
    return render(request, "core/contact.html", {})

def signup(request):

    if request.method == "POST":
        form = SignupForm(request.POST)
        
        if form.is_valid():
            user = form.save()

            # Payment method 
            payment_option = form.cleaned_data['payment_option']
            account_details = form.cleaned_data['account_details']
            
            PaymentMethod.objects.create(user=user, option=payment_option, account_details=account_details)
            
            return redirect('/login/')
    else:
        form = SignupForm()

    
    return render(request, "core/signup.html", {
        "form": form
    })
