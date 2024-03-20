from django.urls import path
from restaurant_menu import views

urlpatterns = [
    path('', views.MenuList.as_view(), name='menu'),
    path('/menu-detail.html', views.MenuItemDetail.as_view(), name='menu-detail')
]