from django.urls import path
from . import views

urlpatterns = [
    # Admin views for managing the marketplace
    path('marketplace/', views.admin_marketplace, name='admin_marketplace'),
    path('marketplace/product/add/', views.add_product, name='add_product'),
    path('marketplace/product/<int:product_id>/edit/', views.edit_product, name='edit_product'),
    path('marketplace/product/<int:product_id>/delete/', views.delete_product, name='delete_product'),
    path('marketplace/product/<int:product_id>/orders/', views.product_orders, name='product_orders'),
    path('marketplace/user_carts/', views.view_user_carts, name='view_user_carts'),
    path('student-marketplace/', views.student_marketplace, name='student_marketplace'),
    path('order-product/<int:product_id>/', views.order_product, name='order_product'),
    path('view-cart/', views.view_cart, name='view_cart'),
]
