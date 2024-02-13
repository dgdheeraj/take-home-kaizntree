from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Tag, Category, Inventory
import json

User = get_user_model()

class AuthenticationTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse('api-register')
        self.login_url = reverse('api-login')
        self.logout_url = reverse('api-logout')
        self.session_url = reverse('api-session')
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_register(self):
        response = self.client.post(self.register_url, {'username': 'newuser', 'password': 'newpassword'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.post(self.register_url, {'username': 'newuser', 'password': 'newpassword'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_login(self):
        # Valid login
        response = self.client.post(self.login_url, {'username': 'testuser', 'password': 'testpassword'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Missing username
        response = self.client.post(self.login_url, {'password': 'testpassword'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Missing password
        response = self.client.post(self.login_url, {'username': 'testuser'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_logout(self):
        # Valid logout
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.logout_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_session(self):
        # Valid session check
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.session_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Trying to check session without being logged in
        self.client.logout()
        response = self.client.get(self.session_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class TagsAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.tag_url = reverse('api-tags')
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_create_tag(self):
        # Valid create tag
        response = self.client.post(self.tag_url, {'name': 'newtag'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Trying to create a tag with missing name
        response = self.client.post(self.tag_url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class CategoryAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.category_url = reverse('api-category')
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_create_category(self):
        # Valid create category
        response = self.client.post(self.category_url, {'name': 'newcategory'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Trying to create a category with missing name
        response = self.client.post(self.category_url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class InventoryAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.inventory_url = reverse('api-inventory')
        self.register_url = reverse('api-register')
        self.login_url = reverse('api-login')

        self.category = Category.objects.create(name='Test Category')
        self.tag1 = Tag.objects.create(name='Tag1')
        self.tag2 = Tag.objects.create(name='Tag2')
        self.inventory1 = Inventory.objects.create(SKU='SKU001', name='Item 1', category=self.category, author='Author 1', in_stock=10, available_stock=5)
        self.inventory1.tags.add(self.tag1)
        self.inventory2 = Inventory.objects.create(SKU='SKU002', name='Item 2', category=self.category, author='Author 2', in_stock=20, available_stock=15)
        self.inventory2.tags.add(self.tag2)

        response = self.client.post(self.register_url, {'username': 'newuser', 'password': 'newpassword'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_inventory(self):
        # response = self.client.post(self.register_url, {'username': 'newuser', 'password': 'newpassword'}, format='json')
        # self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.post(self.login_url, {'username': 'newuser', 'password': 'newpassword'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        response = self.client.get(self.inventory_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
