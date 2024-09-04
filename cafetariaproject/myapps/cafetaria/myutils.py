from .models import Order, OrderItem, CustomerPoint, Transaction

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

def calculate_points(total_price: int):
      # assigns a point per every 100ksh
      
      return total_price // 100

def assign_points(order:Order):
    user=order.user
    total_price = order.total_price
    customer_point, created = CustomerPoint.objects.get_or_create(user=user)
    points = calculate_points(total_price)
    customer_point.points = points
    customer_point.save()

    transaction = Transaction.objects.create(customer_point=customer_point,
                                             amount= total_price,
                                             points_earned=points)
    return transaction

def generate_receipt(order_id):
      # use signals to trigger receipt generation when an order status is
      # changed to complete. Print the receipt from the printer and also send it to the 
      # customer notifications. 
      pass