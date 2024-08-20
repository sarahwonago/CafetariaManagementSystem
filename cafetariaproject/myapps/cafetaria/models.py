from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

User = get_user_model()


class Category(models.Model):
    """
    Defines categories for food items.
    """

    class Meta:
        verbose_name_plural = "Categories"
    
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class FoodItem(models.Model):
    """
    Defines food items.
    """

    class Meta:
        verbose_name_plural = "FoodItems"

    category = models.ForeignKey(
        Category,
        related_name="fooditems",
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=250, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to="food_images/")
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class DiningTable(models.Model):
    """
    Defines the dining tables.
    """

    class Meta:
        verbose_name_plural = "Dining Tables"

    table_number = models.PositiveIntegerField(verbose_name="Table Number", unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Table {self.table_number}"


class Order(models.Model):
    """
    Defines the orders.
    """

    class Meta:
        verbose_name_plural = "Orders"

    
    ESTIMATED_TIME_CHOICES = [(i, f"{i} minutes") for i in range(5, 65, 5)]

    user = models.ForeignKey(
        User,
        related_name="orders",
        on_delete=models.CASCADE
    )
    dining_table = models.ForeignKey(
        DiningTable,
        related_name="orders",
        on_delete=models.CASCADE
    )
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    is_paid = models.BooleanField(default=False)
    estimated_time = models.IntegerField(
        choices=ESTIMATED_TIME_CHOICES,
        help_text="Estimated time in minutes"
    )
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.user.username}"
    
    def calculate_total_price(self):
        """
        Calcualates the total price for all the order items.
        """

        total = 0
        for item in self.orderitems.all():
            total += item.fooditem.price * item.quantity
        return total
    
    def save(self, *args, **kwargs):
        self.total_price = self.calculate_total_price()
        super(Order, self).save(*args, **kwargs)


class OrderItem(models.Model):
    """
    Defines the individual items within an order.
    """

    class Meta:
        verbose_name_plural = "Order Items"
        unique_together = ('order', 'fooditem')

    order = models.ForeignKey(
        Order,
        related_name="orderitems",
        on_delete=models.CASCADE
    )
    fooditem = models.ForeignKey(
        FoodItem,
        related_name="orderitems",
        on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(
        default = 1,
        validators=[MinValueValidator(1)],
        help_text="Quantity of the item"
    )
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} x {self.fooditem.name} (Order {self.order.id})"



class Review(models.Model):
    """
    Defines the reviews for orders.
    """

    class Meta:
        verbose_name_plural = "Reviews"

    user = models.ForeignKey(
        User,
        related_name="reviews",
        on_delete=models.CASCADE
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for Order {self.order.id}"
