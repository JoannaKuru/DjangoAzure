"""suppliers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

# from app.views import landingview, tuplana ku niin pitkä rivi eikä tunnistanu..
from .views import productlistview, supplierlistview, searchproducts, \
    addsupplier, addproduct, deleteproduct, deletesupplier, confirmdeleteproduct, confirmdeletesupplier, \
        products_filtered, edit_product_get, edit_product_post, searchsuppliers, edit_supplier_get, edit_supplier_post, \
             loginview, login_action, logout_action

urlpatterns = [

    #After successful login
    # path('landing/', landingview),

    #LOGIN
    path('', loginview),
    path('login/', login_action),
    path('logout/', logout_action),

    #Product urls
    path('products/', productlistview),
    path('add-product/', addproduct),
    path('delete-product/<int:id>/', deleteproduct),
    path('confirm-delete-product/<int:id>/', confirmdeleteproduct),
    path('products-by-supplier/<int:id>/', products_filtered),
    path('edit-product-get/<int:id>/', edit_product_get),
    path('edit-product-post/<int:id>/', edit_product_post),
    path('search-products/', searchproducts),


    #Supplier urls
    path('suppliers/', supplierlistview),
    path('add-supplier/', addsupplier),
    path('delete-supplier/<int:id>/', deletesupplier),
    path('confirm-delete-supplier/<int:id>/', confirmdeletesupplier),
    path('edit-supplier-get/<int:id>/', edit_supplier_get),
    path('edit-supplier-post/<int:id>/', edit_supplier_post),
    path('search-suppliers/', searchsuppliers),
]
