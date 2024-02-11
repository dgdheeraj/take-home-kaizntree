from django.urls import include, path
from .views import CustomerCreate, CustomerList


urlpatterns = [
    path('create/', CustomerCreate.as_view(), name='create-customer'),
    path('', CustomerList.as_view()),
]