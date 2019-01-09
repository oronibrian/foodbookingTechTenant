from rest_framework import serializers

from orders.models import Order,OrderItem



class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ("order_id","name", "email","phone_number",
         "address","created","updated")
        
        readonly_field=['order_id']


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ("order","product",'quantity','price')
        readonly_field=['price']









