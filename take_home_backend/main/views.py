from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.http import JsonResponse
import json

from .models import Book
from .serializers import BookSerializer

User = get_user_model()


class ListBooksAPI(generics.ListAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class RegisterView(APIView):
    
    def post(self, request):
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        print("in register view")
        print("HERE::",username, password)
        if username is None or password is None:
            return JsonResponse({'detail': 'Please provide username and password.'}, status=400)

        if User.objects.filter(username=username).exists():
            return JsonResponse({'detail': 'Username is already taken.'}, status=400)

        user = User.objects.create_user(username=username, password=password)
        # login(request, user)
        return JsonResponse({'detail': 'User registered'})


class LoginView(APIView):

    def post(self, request):
        """
        API To Login
        """
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        if username is None or password is None:
            return JsonResponse({'detail': 'Please provide username and password.'}, status=400)

        user = authenticate(username=username, password=password)

        if user is None:
            return JsonResponse({'detail': 'Invalid credentials.'}, status=400)

        login(request, user)
        return JsonResponse({'detail': 'Successfully logged in.'})

class LogoutView(APIView):
    def get(self, request):
        """
        API To logout
        """
        if not request.user.is_authenticated:
            return JsonResponse({'detail': 'You\'re not logged in.'}, status=400)

        logout(request)
        return JsonResponse({'detail': 'Successfully logged out.'})


class SessionView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request, format=None):
        return JsonResponse({'isAuthenticated': True})


class WhoAmIView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request, format=None):
        return JsonResponse({'username': request.user.username})