from django.contrib import admin
from .models import Flan, ContactForm, Cart, CartItem

admin.site.register(Flan)
admin.site.register(ContactForm)
admin.site.register(Cart)
admin.site.register(CartItem)