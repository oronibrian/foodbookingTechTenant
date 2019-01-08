from rest_framework import serializers

from orders.models import Order,OrderItem



class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ("id","first_name", "last_name", "email",
         "address", "city","created","updated","paid")
        
        readonly_field=['id','short_description','restaurant']



class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ("order","product",'quantity','price')
        readonly_field=['price']









