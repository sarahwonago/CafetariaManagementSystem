

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import user_passes_test

from .models import Category, FoodItem, Order, OrderItem, UserDinningTable
from .forms import UserDinningForm
from .myutils import calculate_total_price,calculate_total_item_price, increase_orderitem_quantity, decrease_orderitem_quantity


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
def food_items_view(request):

    categories = Category.objects.all()
    

    context = {
        "categories":categories,
        
    }
    return render(request, "cafetaria/food_items.html", context)

@login_required
@user_passes_test(is_customer, login_url='cafetaria:handle_unauthorized_access', redirect_field_name=None)
def addtocart_view(request, food_id):
    user = request.user

    food_item = get_object_or_404(FoodItem, id=food_id)

    order, created = Order.objects.get_or_create(user=user, is_paid = False)
    
    order_item, created = OrderItem.objects.get_or_create(order=order, fooditem=food_item)

    total_price = calculate_total_price(order)
    order.total_price = total_price
    order.save()

    orderitem_total_price = calculate_total_item_price(order_item)
    order_item.total_price = orderitem_total_price
    order_item.save()


    return redirect("cafetaria:food")

@login_required
@user_passes_test(is_customer, login_url='cafetaria:handle_unauthorized_access', redirect_field_name=None)
def cart_view(request):

    user = request.user
    
    try:
        order = Order.objects.get(user=user, is_paid=False)
    except Order.DoesNotExist:
        order = None

    if order is None:
        pass
    
    else:
        total_price = calculate_total_price(order)
        order.total_price = total_price
        order.save()

        for order_item in order.orderitems.all():
            orderitem_total_price = calculate_total_item_price(order_item)
            order_item.total_price = orderitem_total_price
            order_item.save()
    
    context = {
        'order': order,
        }
    
    return render(request, "cafetaria/cart.html", context)


@login_required
@user_passes_test(is_customer, login_url='cafetaria:handle_unauthorized_access', redirect_field_name=None)
def checkout_view(request):
    user=request.user
    order = get_object_or_404(Order, user=user, is_paid=False)

    # processs payment here

    order.is_paid = True 
    order.save()
    user_dinning = UserDinningTable.objects.get(user = user)
    table = user_dinning.dinning_table.table_number


    return redirect("cafetaria:order-complete", order.id)

@login_required
@user_passes_test(is_customer, login_url='cafetaria:handle_unauthorized_access', redirect_field_name=None)
def order_complete_view(request, order_id):

    order = get_object_or_404(Order, id=order_id)

    context = {
        "order": order
    }

    return render(request, 'cafetaria/order_complete.html', context)


@login_required
@user_passes_test(is_customer, login_url='cafetaria:handle_unauthorized_access', redirect_field_name=None)
def increase_orderitem_view(request, item_id):

    orderitem = get_object_or_404(OrderItem, id=item_id)
    orderitem = increase_orderitem_quantity(orderitem)

    return redirect("cafetaria:cart")


@login_required
@user_passes_test(is_customer, login_url='cafetaria:handle_unauthorized_access', redirect_field_name=None)
def decrease_orderitem_view(request, item_id):

    orderitem = get_object_or_404(OrderItem, id=item_id)
    orderitem = decrease_orderitem_quantity(orderitem)

    return redirect("cafetaria:cart")


@login_required
@user_passes_test(is_customer, login_url='cafetaria:handle_unauthorized_access', redirect_field_name=None)
def remove_item_view(request, item_id):

    orderitem = get_object_or_404(OrderItem, id=item_id)
    order = orderitem.order
    orderitem.delete()

    if order.orderitems.count() == 0:
        order.delete()
    
    return redirect("cafetaria:cart")


@login_required
@user_passes_test(is_customer, login_url='cafetaria:handle_unauthorized_access', redirect_field_name=None)
def order_history_view(request):
    user = request.user

    try:
        past_orders = get_list_or_404(Order, user=user, is_paid=True, status="COMPLETE")
    except:
        past_orders = None


    try:
        p_order = get_object_or_404(Order, user=user, is_paid=True, status="PENDING")
    except:
        p_order = None

    context = {
        "past_orders":past_orders,
        "p_order": p_order,
    }

    return render(request, 'cafetaria/order_history.html', context)

@login_required
@user_passes_test(is_customer, login_url='cafetaria:handle_unauthorized_access', redirect_field_name=None)
def order_receipt_view(request, order_id):
    order = get_object_or_404(Order, id = order_id)

    context = {
        "order":order,
    }

    return render(request, 'cafetaria/order_reciept.html', context)