from .models import Order, OrderItem

def calculate_total_price(order:Order):
        """
        Calcualates the total price for all the order items.
        """

        total = 0
        for item in order.orderitems.all():
            total += item.fooditem.price * item.quantity
        return total

def update_orderitem_quantity(orderitem:OrderItem):
      """
        Updates order item quantity.
      """
      
      return orderitem