from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product, Cart
from .forms import ProductForm, OrderForm
from accounts.decorators import role_required

"""
STUDENT-SIDE VIEWS

Improvements: 
    1. Students can verify if their order is still pending, received or cancelled
    2. Students can edit their orders, or even cancel it
    3. Stocks must reduce upon orders of students
"""

@login_required
@role_required('student')
def student_marketplace(request):
    """
    Responsible for listing all of the products
    """
    products = Product.objects.all()
    return render(request, 'marketplace/student/student_marketplace.html', {'products': products})

# View to order a product
@login_required
@role_required('student')
def order_product(request, product_id):
    """
    Responsible for ordering products from the table
    """
    product = get_object_or_404(Product, product_id=product_id)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.product = product
            if product.is_stock_available(order.quantity):
                order.save()
                return redirect('view_cart')
            else:
                form.add_error(None, "Insufficient stock available")
    else:
        form = OrderForm()

    return render(request, 'marketplace/student/order_product.html', {'form': form, 'product': product})

# View to see the student's cart
@login_required
@role_required('student')
def view_cart(request):
    """
    Responsible for viewing the cart of the user
    """
    cart_items = Cart.objects.filter(user=request.user)
    return render(request, 'marketplace/student/view_cart.html', {'cart_items': cart_items})


"""
ADMIN-SIDE VIEWS

Improvements: 
    1. Admins can have search functions, specifically in the 'View Cart', to target specific students
    2. Admins can clearly see the state of an order (Pending, Received, Cancelled) or even delete a cancelled order
    3. Admins can confirm upon deleting products
"""

# Admin-only view to manage products (Add, Edit, Delete)
@login_required
@role_required('admin')
def admin_marketplace(request):
    """
    Responsible for acquiring the lists of products 
    """
    if not request.user.role == 'admin':
        return redirect('student_dashboard')  # If not admin, redirect to student dashboard

    products = Product.objects.all()
    return render(request, 'marketplace/admin/admin_marketplace.html', {'products': products})

# View to add a new product
@login_required
@role_required('admin')
def add_product(request):
    """
    Responsible for adding the products to the database
    """
    if not request.user.role == 'admin':
        return redirect('student_dashboard')

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_marketplace')  # Redirect to the marketplace page
    else:
        form = ProductForm()

    return render(request, 'marketplace/admin/add_product.html', {'form': form})

# View to edit a product
@login_required
@role_required('admin')
def edit_product(request, product_id):
    """
    Responsible for editing the product's information
    """
    if not request.user.role == 'admin':
        return redirect('student_dashboard')

    product = get_object_or_404(Product, product_id=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('admin_marketplace')
    else:
        form = ProductForm(instance=product)

    return render(request, 'marketplace/admin/edit_product.html', {'form': form})

# View to delete a product
@login_required
@role_required('admin')
def delete_product(request, product_id):
    """
    Responsible for deleting the product from the database
    """
    if not request.user.role == 'admin':
        return redirect('student_dashboard')

    product = get_object_or_404(Product, product_id=product_id)
    product.delete()
    return redirect('admin_marketplace')

# View to see all orders for a product
@login_required
@role_required('admin')
def product_orders(request, product_id):
    """
    Responsible for displaying the orders in a specific product
    """
    if not request.user.role == 'admin':
        return redirect('student_dashboard')

    product = get_object_or_404(Product, product_id=product_id)
    orders = Cart.objects.filter(product=product)
    
    return render(request, 'marketplace/admin/product_orders.html', {'product': product, 'orders': orders})

# View to see all user carts
@login_required
@role_required('admin')
def view_user_carts(request):
    """
    Responsible for displaying the carts of the users 
    """
    if not request.user.role == 'admin':
        return redirect('student_dashboard')

    carts = Cart.objects.all()
    return render(request, 'marketplace/admin/user_carts.html', {'carts': carts})
