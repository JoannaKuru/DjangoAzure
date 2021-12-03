from django.test import TestCase
import unittest

from .laskin import plus

class LaskinTests(TestCase):
    def test_plus(self):
        # testaa että numerot lasketaan yhteen oikein, TestCasen metodi assertEqual:
        self.assertEqual(plus(7, 2), 9)

    def test_plus_string(self):
        # testaa että numerot lasketaan yhteen oikein, TestCasen metodi assertEqual:
        self.assertEqual(plus("700", "200"), 900)
    #Jos laittaa väärän luvun, niin ilmoittaa failuresta ja syyn!

    @unittest.expectedFailure
    def test_plus_should_fail(self):
        self.assertEqual(plus(7, 3), "teppo")

#   # Alla oleva ei vaatisi mitään importtia!
#     def test_plus1(self):
#         # testaa että numerot lasketaan yhteen oikein, TestCasen metodi assertEqual:
#         self.assertEqual(9, 9)
#         #tai 8, jolloin testi ei onnistu!!



















'''
from django.http import response
from django.test import TestCase, Client, client
import unittest
from django.urls import reverse
from .laskin import plus
from .models import Supplier, Product
from .views import supplierlistview, productlistview
client = Client()
class ListMethodTests(TestCase):

    def test_listing_products(self):
        palauttaa statuskoodin 200
        response = client.get(reverse(productlistview))
        self.assertEqual(response.status_code, 200)


class SupplierModelTests(TestCase):

    def setUp(self):
        Supplier.objects.create(companyname="Test company", contactname="Jaakko Kulta", address="Kultatie 1", phone="12345567", email="jaakko@kulta.fi", country="Finland")

    def test_added_supplier_exists(self):
        """Added supplier exists and can be searched"""
        supplier = Supplier.objects.get(companyname="Test company")
        self.assertEqual(supplier.address, "Kultatie 1")
        self.assertEqual(supplier.country, "Finland")


class LaskinTests(TestCase):

    def test_plus(self):
        # testaa että numerot lasketaan yhteen oikein
        self.assertEqual(plus(7, 2), 9)

    def test_plus_string(self):
        # testaa että numerot lasketaan yhteen oikein
        self.assertEqual(plus("7", "2"), 9)

    @unittest.expectedFailure
    def test_plus_should_fail(self):
        self.assertEqual(plus(7, 3), "teppo")
'''
