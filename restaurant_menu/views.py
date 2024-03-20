from django.shortcuts import render
from django.views import generic

from restaurant_menu.models import Item


class MenuList(generic.ListView):
    queryset = Item.objects.order_by("date_created")
    template_name = "index.html"

class MenuItemDetail(generic.DetailView):
    model = Item
    template_name = "menu-detail.html"
