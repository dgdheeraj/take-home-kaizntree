from django.shortcuts import render
from .models import Customer
from rest_framework import generics
from .serializers import CustomerSerializer


class CustomerCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new customer
    queryset = Customer.objects.all(),
    serializer_class = CustomerSerializer


class CustomerList(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer