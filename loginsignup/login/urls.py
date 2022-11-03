from django.urls import path
from .views import LoginView, LogoutView,HomeView

urlpatterns = [
    path('login/', LoginView.as_view(),name='account_login'),
    path('logout/', LogoutView.as_view(), name='account_logout'),
    path('', HomeView.as_view(),name='home')
]