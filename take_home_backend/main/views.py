from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.http import JsonResponse
from django.core.exceptions import FieldError
import json

from .models import Tag, Category, Inventory
from .serializers import TagSerializer, CategorySerializer, InventorySerializer 

User = get_user_model()

"""
Authentication APIs
"""

class RegisterView(APIView):
    def post(self, request):
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        if username is None or password is None:
            return JsonResponse({'detail': 'Please provide username and password.'}, status=400)

        if User.objects.filter(username=username).exists():
            return JsonResponse({'detail': 'Username is already taken.'}, status=400)

        user = User.objects.create_user(username=username, password=password)
        return JsonResponse({'detail': 'User registered'})


class LoginView(APIView):
    def post(self, request):
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
        # if not request.user.is_authenticated:
        #     return JsonResponse({'detail': 'You\'re not logged in.'}, status=400)

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


"""
APIs for Tags, Category, Inventory
"""

class TagsAPI(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        queryset = Tag.objects.all()
        serializer = TagSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'detail': 'Created'}, status=201)
        
        return JsonResponse({'detail': 'Error creating item'}, status=400)


class CategoryAPI(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        print(request.user.is_authenticated,"HERE!!!!!")
        return JsonResponse(serializer.data, safe=False)
        
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'detail': 'Created'}, status=201)
        
        return JsonResponse({'detail': 'Error creating item'}, status=400)


class InventoryAPI(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Filtering Options
        """
        sku_param = self.request.query_params.get('sku')
        name_param = self.request.query_params.get('name')
        category_param = self.request.query_params.get('category')
        tag_param = self.request.query_params.get('tag')
        sort_param = self.request.query_params.get('sort_by')
        order_param = self.request.query_params.get('order')
        stock_status_param = self.request.query_params.get('stock_status')
        queryset = Inventory.objects.all()
        
        try:
            if sku_param:
                queryset = queryset.filter(SKU__contains=sku_param)
            if category_param:
                queryset = queryset.filter(category__name__contains=category_param)
            if name_param:
                queryset = queryset.filter(name__contains=name_param)
            if tag_param:
                queryset = queryset.filter(tags__name__contains=tag_param)
            if stock_status_param:
                stock_status_param = float(stock_status_param)
                queryset = queryset.filter(in_stock__contains=stock_status_param)
            if sort_param:
                if order_param == "desc":
                    sort_param = f"-{sort_param}"
                    queryset = queryset.order_by(sort_param)      

        except FieldError as e:
            return JsonResponse({'detail': str(e)}, status=400)
        except ValueError as e:
            return JsonResponse({'detail': str(e)}, status=400)
        
        serializer = InventorySerializer(queryset, many=True)

        for raw_data in serializer.data:
            # Category
            cid = raw_data.get('category', None)
            category_doc = Category.objects.get(id=cid)
            if category_doc == None:
                return JsonResponse({'detail': 'cant find category'}, status=400)
            
            raw_data['category'] = category_doc.name

            # Tags
            tag_names = []
            tids = raw_data.get('tags', None)
            for tid in tids:
                tag_doc = Tag.objects.get(id=tid)
                if tag_doc == None:
                    return JsonResponse({'detail': 'cant find tag'}, status=400)
                tag_names.append(tag_doc.name)

            raw_data['tags'] = tag_names

        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        in_data = request.data

        category_name = in_data.get('category', None)
        if category_name == None:
            return JsonResponse({'detail': 'Error creating item, no category name'}, status=400)
        
        category_doc = Category.objects.get(name=category_name)
        if category_doc == None:
            return JsonResponse({'detail': 'Error creating item, invalid category'}, status=400)

        in_data['category'] = category_doc.id

        tags_names = in_data.get('tags', None)
        if tags_names == None:
            return JsonResponse({'detail': 'Error creating item, no tags'}, status=400)
        
        tids = []
        for tn in tags_names:
            tag_doc = Tag.objects.get(name=tn)
            if tag_doc == None:
                return JsonResponse({'detail': 'Error creating item, invalid tag found'}, status=400)
            tids.append(tag_doc.id)

        in_data['tags'] = tids
        
        serializer = InventorySerializer(data=in_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'detail': 'Created'}, status=201)
        
        return JsonResponse({'detail': 'Error creating item'}, status=400)