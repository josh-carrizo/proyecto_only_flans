"""
URL configuration for onlyflans project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from producto.views import index, about, welcome, contacto, success,register, ver_carrito, agregar_al_carrito, eliminar_del_carrito,productos
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('acerca/', about, name='about'),
    path('bienvenido/', welcome, name='welcome'),
    path('contacto/', contacto, name='contacto'),
    path('success/', success, name='success'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
    path('register/', register, name='register'),
    path('carrito/', ver_carrito, name='ver_carrito'),
    path('carrito/agregar/<int:flan_id>/', agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/eliminar/<int:item_id>/',eliminar_del_carrito, name='eliminar_del_carrito'),
    path('productos/', productos, name='productos'),

]