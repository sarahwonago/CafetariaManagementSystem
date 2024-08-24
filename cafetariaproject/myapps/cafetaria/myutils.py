from .models import Order, OrderItem

def calculate_total_price(order:Order):
        """
        Calculates the total price for all the order items.
        """

        total = 0
        for item in order.orderitems.all():
            total += item.fooditem.price * item.quantity
        return total

def calculate_total_item_price(item:OrderItem):
        """
        Calculates the  item total price.
        """

        item_total = item.fooditem.price * item.quantity
        return item_total

def increase_orderitem_quantity(orderitem:OrderItem):
      """
        Increase order item quantity by 1.
      """
      orderitem.quantity += 1
      orderitem.save()
      return orderitem

def decrease_orderitem_quantity(orderitem:OrderItem):
      """
        Decreases order item quantity by 1.
      """
      if orderitem.quantity == 1:
            return orderitem
      
      orderitem.quantity -= 1
      orderitem.save()

      return orderitem