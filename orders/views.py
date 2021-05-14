from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from orders.models import Order, Customer
from orders.serializers import OrderSerializer, CustomerSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows orders to be viewed or edited
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @action(detail=False)
    def status_list(self, request):
        all_statuses = Order.objects.all().order_by('-status')

        page = self.paginate_queryset(all_statuses)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(all_statuses, many=True)
        return Response(serializer.data)


class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows customers to be viewed or edited
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
