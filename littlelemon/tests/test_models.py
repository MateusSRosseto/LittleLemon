from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(Title = "Burger", Price = 5.00, Inventory = 30)
        self.assertEqual(item.__str__(), "Burger : 5.0")