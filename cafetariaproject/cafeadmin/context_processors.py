from myapps.cafetaria.models import Order

def cart_item_count(request):
    if request.user.is_authenticated:
        try:
            order = Order.objects.get(user=request.user, is_paid=False)
            item_count = order.orderitems.count()
        except Order.DoesNotExist:
            item_count = 0
    else:
        item_count=None
    context = {
        "cart_item_count": item_count
    }
    return context
