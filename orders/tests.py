import json
import random

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from orders.models import Customer, Order


class GetCustomerTestCase(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.customer1 = Customer.objects.create(first_name='Christopher', last_name='Columbus')
        self.customer2 = Customer.objects.create(first_name='Bruce', last_name='Willis')

    def test_get_all_customers(self):
        customers_url = reverse('orders:customer-list')
        response = self.client.get(customers_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'first_name', count=2)

    def test_get_one_customer(self):
        customer_url = reverse('orders:customer-detail', args=[self.customer1.id])
        print(customer_url)
        response = self.client.get(customer_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetOrderTestCase(TestCase):
    def setUp(self) -> None:
        valid_sizes = Order.PIZZA_SIZE[1:]
        valid_flavors = Order.FLAVOR[1:]

        self.customer1 = Customer.objects.create(first_name='Marco', last_name='Polo')
        self.customer2 = Customer.objects.create(first_name='Johnny', last_name='Depp')
        self.order1 = Order.objects.create(
            customer=self.customer1,
            size=random.choice(valid_sizes),
            flavor=random.choice(valid_flavors),
        )
        self.order2 = Order.objects.create(
            customer=self.customer2,
            size=random.choice(valid_sizes),
            flavor=random.choice(valid_flavors),
            count=3,
        )
        self.order3 = Order.objects.create(
            customer=self.customer2,
            size=Order.PIZZA_SIZE[1][0],
            flavor=Order.FLAVOR[2][0],
            count=4,
        )

    def test_get_all_orders(self):
        orders_url = reverse('orders:order-list')
        response = self.client.get(orders_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'status', count=3)

    def test_get_one_order(self):
        order_url = reverse('orders:order-detail', args=[self.order1.id])
        print(order_url)
        response = self.client.get(order_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Marco')

    def test_order_same_flavor_different_sizes(self):
        # Confirm order3 created by customer2 is okay
        order3_url = reverse('orders:order-detail', args=[self.order3.id])
        response = self.client.get(order3_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['size'], Order.PIZZA_SIZE[1][0])
        self.assertEqual(response.data['flavor'], Order.FLAVOR[2][0])
        self.assertEqual(response.data['count'], 4)

        # Create order4 by the same customer2 with different size, flavor and count and confirm
        order4 = Order.objects.create(
            customer=self.customer2,
            size=Order.PIZZA_SIZE[3][0],
            flavor=Order.FLAVOR[3][0],
            count=5,
        )
        order4_url = reverse('orders:order-detail', args=[order4.id])
        response = self.client.get(order4_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['size'], Order.PIZZA_SIZE[3][0])
        self.assertEqual(response.data['flavor'], Order.FLAVOR[3][0])
        self.assertEqual(response.data['count'], 5)

    def test_update_order_succeeds_on_status_submitted(self):
        data = {
            'customer': {
                'first_name': 'Johnny',
                'last_name': 'Depp'
            },
            'size': Order.PIZZA_SIZE[2][0],
            'flavor': Order.FLAVOR[1][0],
            'count': 1,
            'status': Order.ORDER_STATUS[0][0],
        }
        response = self.client.put(
            reverse('orders:order-detail', args=[self.order3.id]),
            data=data,
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['size'], Order.PIZZA_SIZE[2][0])
        self.assertEqual(response.data['flavor'], Order.FLAVOR[1][0])
        self.assertEqual(response.data['count'], 1)

    def test_update_order_fails_on_status_delivered(self):
        data = {
            'size': Order.PIZZA_SIZE[2][0],
            'flavor': Order.FLAVOR[1][0],
            'count': 1,
            'status': Order.ORDER_STATUS[1][0],
        }
        response = self.client.patch(
            reverse('orders:order-detail', args=[self.order3.id]),
            data=data,
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Order retains previous values
        self.assertEqual(response.data['size'], Order.PIZZA_SIZE[1][0])
        self.assertEqual(response.data['flavor'], Order.FLAVOR[2][0])
        self.assertEqual(response.data['count'], 4)
