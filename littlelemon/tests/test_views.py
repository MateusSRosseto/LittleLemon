from django.test import TestCase
from restaurant.models import Menu


class MenuViewSet(TestCase):
    def setUp(self):
        Menu.objects.create(Title = 'IceCream', Price = 2.00, Inventory = 3)
        Menu.objects.create(Title = 'Cake', Price = 7.00, Inventory = 5)
        
    def test_getall(self):
        instance1 = Menu.objects.get(Title = 'IceCream')
        instance2 = Menu.objects.get(Title = 'Cake')
        self.assertEqual(instance1.__str__(), "IceCream : 2.00")
        self.assertEqual(instance2.__str__(), "Cake : 7.00")