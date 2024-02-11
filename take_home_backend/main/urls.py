from django.urls import include, path
from . import views


urlpatterns = [
    path('books/', views.ListBooksAPI.as_view(), name='list-books'),
    path('register/', views.RegisterView.as_view(), name='api-login'),
    path('login/', views.LoginView.as_view(), name='api-login'),
    path('logout/', views.LogoutView.as_view(), name='api-logout'),
    path('session/', views.SessionView.as_view(), name='api-session'),
    path('whoami/', views.WhoAmIView.as_view(), name='api-whoami'),
]