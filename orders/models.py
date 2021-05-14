from django.core.validators import MinValueValidator
from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Order(models.Model):
    ORDER_STATUS = (
        ('SUBMITTED', 'Submitted'),
        ('PRODUCTION', 'In Production'),
        ('DELIVERING', 'Left to Deliver'),
        ('DELIVERED', 'Delivered'),
        ('CANCELLED', 'Cancelled'),
    )
    PIZZA_SIZE = (
        (None, 'Select a size'),
        ('SMALL', 'Small'),
        ('MEDIUM', 'Medium'),
        ('LARGE', 'Large'),
    )
    FLAVOR = (
        (None, 'Select a flavor'),
        ('MARGARITA', 'Margarita'),
        ('MARINARA', 'Marinara'),
        ('SALAMI', 'Salami'),
    )

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    size = models.CharField(max_length=50, choices=PIZZA_SIZE, blank=False, null=False)
    flavor = models.CharField(max_length=30, choices=FLAVOR, blank=False, null=False)
    count = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)], blank=False, null=False, default=1)
    status = models.CharField(max_length=30, choices=ORDER_STATUS, blank=False, null=False, default='SUBMITTED')

    def __str__(self):
        return f'{self.customer} -> {self.get_flavor_display()}'
