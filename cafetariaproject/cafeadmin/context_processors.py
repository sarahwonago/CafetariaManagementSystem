from myapps.cafetaria.models import Order, Notification
from django.utils import timezone

def cart_item_count(request):
    if request.user.is_authenticated:
        notifications = Notification.objects.filter(user=request.user, is_read=False).count()
        try:
            order = Order.objects.get(user=request.user, is_paid=False)
            item_count = order.orderitems.count()
        except Order.DoesNotExist:
            item_count = 0
    else:
        item_count=None
    context = {
        "cart_item_count": item_count,
        "notification":notifications,
    }
    return context



def current_date(request):
    return {
        'today': timezone.now().date()
    }

