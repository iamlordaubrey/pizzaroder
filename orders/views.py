from rest_framework import viewsets

from orders.models import Order, Customer
from orders.serializers import OrderSerializer, CustomerSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows orders to be viewed or edited
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows customers to be viewed or edited
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
