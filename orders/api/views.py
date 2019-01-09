from django.shortcuts import render
from orders.models import Order,OrderItem
from rest_framework import generics,mixins
from .serializer import OrderSerializer,OrderItemSerializer
from django.db.models import Q

class OrderCreateView(mixins.CreateModelMixin,generics.ListAPIView):
	lookup_field='pk'

	serializer_class=OrderSerializer

	def get_queryset(self):
		qs=Order.objects.all()
		query=self.request.GET.get('q')
		if query is not None:
			qs=qs.filter(Q(name__icontains=query)|Q(address__icontains=query)).distinct()

		return qs



	def post(self,request,*args,**kwargs):
		return self.create(request,*args,**kwargs)

class OrderRUDView(generics.RetrieveUpdateDestroyAPIView):
	lookup_field='pk'

	serializer_class=OrderSerializer

	def get_queryset(self):
		return Order.objects.all()



