from rest_framework import serializers

from orders.models import Order, Customer


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='orders:customer-detail')

    class Meta:
        model = Customer
        fields = '__all__'


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    customer = CustomerSerializer()
    url = serializers.HyperlinkedIdentityField(view_name='orders:order-detail')

    class Meta:
        model = Order
        fields = '__all__'

    def update(self, instance, validated_data):
        status_can_update_order = ['SUBMITTED']
        status_with_fixed_order = [x[0] for x in Order.ORDER_STATUS if x[0] not in status_can_update_order]
        instance.status = validated_data.get('status', instance.status)
        if instance.status in status_with_fixed_order:
            return instance

        instance.flavor = validated_data.get('flavor', instance.flavor)
        instance.count = validated_data.get('count', instance.count)
        instance.size = validated_data.get('size', instance.size)

        instance.save()

        return instance
