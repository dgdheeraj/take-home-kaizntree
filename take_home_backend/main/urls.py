from django.urls import include, path
from . import views


urlpatterns = [
    path('tags/', views.TagsAPI.as_view(), name='tags'),
    path('category/', views.CategoryAPI.as_view(), name='category'),
    path('inventory/', views.InventoryAPI.as_view(), name='inventory'),
    path('register/', views.RegisterView.as_view(), name='api-login'),
    path('login/', views.LoginView.as_view(), name='api-login'),
    path('logout/', views.LogoutView.as_view(), name='api-logout'),
    path('session/', views.SessionView.as_view(), name='api-session'),
    path('whoami/', views.WhoAmIView.as_view(), name='api-whoami'),
]