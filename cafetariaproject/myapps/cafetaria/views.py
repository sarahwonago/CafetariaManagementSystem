

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test

from .models import Category, FoodItem, Order, OrderItem, UserDinningTable
from .forms import UserDinningForm


#  defines a role based  redirect function for customers
def is_customer(user):
    if user.is_authenticated and user.role == 'customer':
        return True
    if user.is_authenticated and user.role == 'admin':
        return False
    return False

# Custom view to handle unauthorized access for both roles
def handle_unauthorized_access(request):

    """
    Redirect logged-in users to their respective homepages if they are
    already authenticated but trying to access an unauthorized view.
    """
    
    user = request.user
    if user.role == 'customer':
        return redirect('cafetaria:home')
    elif user.role == 'admin':
        return redirect('cafeadmin:home')
    else:
        return redirect('login')
    
@login_required
@user_passes_test(is_customer, login_url='cafetaria:handle_unauthorized_access', redirect_field_name=None)
def home_view(request):

    """
    Renders the home page for authenticated users.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered home page.
    """
    user = request.user

    user_dinning_table, created = UserDinningTable.objects.get_or_create(user=user)

    if request.method == 'POST':
        form = UserDinningForm(request.POST, instance=user_dinning_table)

        if form.is_valid:
            form.save()
            return redirect("cafetaria:food")
    else:
        form = UserDinningForm(instance=user_dinning_table)

    context = {
        "form": form,
    }
    return render(request, "cafetaria/home.html", context)


@login_required
@user_passes_test(is_customer, login_url='cafetaria:handle_unauthorized_access', redirect_field_name=None)
def customer_view(request):

    categories = Category.objects.all()

    context = {
        "categories":categories,
        
    }
    return render(request, "cafetaria/customer.html", context)

@login_required
@user_passes_test(is_customer, login_url='cafetaria:handle_unauthorized_access', redirect_field_name=None)
def addtocart_view(request, food_id):
    user = request.user
    food_item = get_object_or_404(FoodItem, id=food_id)

    order, created = Order.objects.get_or_create(user=user, is_paid = False)
    order.save()
    order_item, created = OrderItem.objects.get_or_create(order=order, fooditem=food_item)
    order_item.save()

    return redirect("/")

@login_required
@user_passes_test(is_customer, login_url='cafetaria:handle_unauthorized_access', redirect_field_name=None)
def order_summary_view(request):

    user = request.user
    order = get_object_or_404(Order, user=user, is_paid=False)

    context = {
        'order': order
        }
    return render(request, 'cafeteria/order_summary.html', context)