from django.shortcuts import render, redirect,get_object_or_404
from .models import Flan, Cart, CartItem
from .forms import ContactFormModelForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.db.models import Sum


def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False) 
    context = {
        'flanes': flanes_publicos
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

@login_required
def welcome(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    context = {
        'flanes': flanes_privados,
        'user': request.user
    }
    return render(request, 'welcome.html', context)

def contacto(request):
    if request.method == 'POST':
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ContactFormModelForm()
    return render(request, 'contacto.html', {'form': form})

def success(request):
    return render(request, 'success.html', {'message': 'Gracias por contactarte con OnlyFlans, te responderemos en breve.'})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def agregar_al_carrito(request, flan_id):
    flan = get_object_or_404(Flan, id=flan_id)
    carrito, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=carrito, flan=flan)

    if not created: 
        cart_item.quantity += 1
        cart_item.save()
    else:
        cart_item.quantity = 1
        cart_item.save()

    return redirect('ver_carrito')


@login_required
def ver_carrito(request):
    carrito = Cart.objects.filter(user=request.user).first()
    total = carrito.items.aggregate(total=Sum('flan__price'))['total'] or 0  

    return render(request, 'ver_carrito.html', {'carrito': carrito, 'total': total})

@login_required
def eliminar_del_carrito(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    if item.cart.user == request.user:
        item.delete()
    
    return redirect('ver_carrito')

def productos(request):
    flanes = Flan.objects.all()
    return render(request, 'productos.html', {'flanes': flanes})