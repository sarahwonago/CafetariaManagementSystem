from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from .views import home_view
from .models import Category, FoodItem, Order, OrderItem, Review, DiningTable

User = get_user_model()


class HomeViewTests(TestCase):
    """
    Tests for the home_view.
    """

    def setUp(self):
        """
        Create a user for authenticated tests.
        """
        self.user = User.objects.create_user(
            username="username",
            password="securepassword123"

        )
        self.login_url = reverse("login")
        self.home_url = reverse("cafetaria:home")

    def test_home_view_accessible_by_authenticated_user(self):
        """
        Test that the home view is accessible to authenticated users.
        """
        self.client.login(username='username', password='securepassword123')
        response = self.client.get(self.home_url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cafetaria/home.html')

        #tests that home url name resolves to home view function
        self.assertTrue(resolve(self.home_url).func, home_view)

    def test_home_view_redirects_unauthenticated_user(self):
        """
        Test that the home view redirects unauthenticated users to the login page.
        """
        response = self.client.get(self.home_url)
        self.assertRedirects(response, f'{self.login_url}?next={self.home_url}')


class CategoryModelTest(TestCase):
    """
    Tests for the model Category.
    """

    def setUp(self):
        """
        Set up function for the model Category.
        """
        self.category = Category.objects.create(
            name = "Beverages",
            description = "Soft drinks, juices and water"
        )

    def test_category_creation(self):
        self.assertEqual(self.category.name, "Beverages")
        self.assertEqual(self.category.description, "Soft drinks, juices and water")
        self.assertIsInstance(self.category.created_at, type(self.category.updated_at))
        self.assertEqual(str(self.category), self.category.name)
        self.assertEqual(Category.objects.count(), 1)

    
# class FoodItemModelTest(TestCase):

#     def setUp(self):
#         self.category = Category.objects.create(name="Snacks", description="Fast food and snacks")
#         self.food_item = FoodItem.objects.create(
#             category=self.category,
#             name="Burger",
#             price=5.99,
#             image="food_images/burger.jpg",
#             description="A delicious beef burger"
#         )

#     def test_fooditem_creation(self):
#         self.assertEqual(self.food_item.name, "Burger")
#         self.assertEqual(self.food_item.price, 5.99)
#         self.assertEqual(self.food_item.description, "A delicious beef burger")
#         self.assertEqual(self.food_item.category, self.category)
#         self.assertEqual(str(self.food_item), self.food_item.name)


# class DiningTableModelTest(TestCase):

#     def setUp(self):
#         self.table = DiningTable.objects.create(table_number=10)

#     def test_diningtable_creation(self):
#         self.assertEqual(self.table.table_number, 10)
#         self.assertEqual(str(self.table), "Table 10")


# class OrderModelTest(TestCase):

#     def setUp(self):
#         self.user = User.objects.create_user(username="testuser", password="password")
#         self.table = DiningTable.objects.create(table_number=1)
#         self.category = Category.objects.create(name="Main Course", description="Main dishes")
#         self.food_item = FoodItem.objects.create(
#             category=self.category,
#             name="Pizza",
#             price=10.00,
#             description="Cheese pizza"
#         )
#         self.order = Order.objects.create(
#             user=self.user,
#             dining_table=self.table,
#             estimated_time=30
#         )

#     def test_order_creation(self):
#         self.assertEqual(self.order.user, self.user)
#         self.assertEqual(self.order.dining_table, self.table)
#         self.assertEqual(self.order.is_paid, False)
#         self.assertEqual(self.order.is_completed, False)
#         self.assertEqual(self.order.estimated_time, 30)
#         self.assertEqual(self.order.total_price, 0.00)

#     def test_order_total_price_calculation(self):
#         # Adding items to the order
#         OrderItem.objects.create(order=self.order, fooditem=self.food_item, quantity=2)
#         self.order.save()

#         self.order.refresh_from_db()
#         self.assertEqual(self.order.total_price, 20.00)


# class OrderItemModelTest(TestCase):

#     def setUp(self):
#         self.user = User.objects.create_user(username="testuser", password="password")
#         self.table = DiningTable.objects.create(table_number=1)
#         self.category = Category.objects.create(name="Appetizers", description="Starters")
#         self.food_item = FoodItem.objects.create(
#             category=self.category,
#             name="Garlic Bread",
#             price=3.50,
#             description="Crispy garlic bread"
#         )
#         self.order = Order.objects.create(
#             user=self.user,
#             dining_table=self.table,
#             estimated_time=20
#         )
#         self.order_item = OrderItem.objects.create(
#             order=self.order,
#             fooditem=self.food_item,
#             quantity=3
#         )

#     def test_orderitem_creation(self):
#         self.assertEqual(self.order_item.order, self.order)
#         self.assertEqual(self.order_item.fooditem, self.food_item)
#         self.assertEqual(self.order_item.quantity, 3)
#         self.assertEqual(str(self.order_item), f"3 x {self.food_item.name} (Order {self.order.id})")


# class ReviewModelTest(TestCase):

#     def setUp(self):
#         self.user = User.objects.create_user(username="testuser", password="password")
#         self.table = DiningTable.objects.create(table_number=1)
#         self.order = Order.objects.create(
#             user=self.user,
#             dining_table=self.table,
#             estimated_time=30
#         )
#         self.review = Review.objects.create(
#             user=self.user,
#             order=self.order,
#             rating=4,
#             comment="Great service!"
#         )

#     def test_review_creation(self):
#         self.assertEqual(self.review.user, self.user)
#         self.assertEqual(self.review.order, self.order)
#         self.assertEqual(self.review.rating, 4)
#         self.assertEqual(self.review.comment, "Great service!")
#         self.assertEqual(str(self.review), f"Review for Order {self.order.id}")

#     def test_rating_validator(self):
#         with self.assertRaises(ValidationError):
#             review = Review(user=self.user, order=self.order, rating=6, comment="Bad")
#             review.full_clean()