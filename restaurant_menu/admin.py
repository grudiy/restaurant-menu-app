from django.contrib import admin
from restaurant_menu.models import Item


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("meal_id", "meal", "status")
    list_filter = ("meal_id", "status")
    search_fields = ("meal_id", "meal", "description")


admin.site.register(Item, MenuItemAdmin)
