from django.contrib import admin
from .models import PaymentMethod, PaymentOption

# Register your models here.
admin.site.register(PaymentOption)
admin.site.register(PaymentMethod)