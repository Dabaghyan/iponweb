from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Buyer, StoreCategory, ItemCategory, Customer, Item
    # ,Store, StoreOwner, MyBag, Purchase


class BuyerAdmin(admin.ModelAdmin):
    list_display = ("id", "registrated_at", "user_info")

    def user_info(self, obj):
        return "{}".format(" ".join(list(obj.user.first_name, obj.user.last_name)))

admin.site.register(Buyer, BuyerAdmin)


class StoreCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'picture')
#
admin.site.register(StoreCategory, StoreCategoryAdmin)
#
#
class ItemCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'picture')

admin.site.register(ItemCategory, ItemCategoryAdmin)
#
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar', 'registered_at')

admin.site.register(Customer, CustomerAdmin)
#
#
# class StoreOwnerAdmin(admin.ModelAdmin):
#     list_display = ('user', 'avatar', 'registered_at')
#
# admin.site.register(StoreOwnerAdmin, StoreOwner)
#
# class StoreAdmin(admin.ModelAdmin):
#     list_display = ('name', 'owner', 'store_category')
#
# admin.site.register(StoreAdmin, Store)
#
#
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'quantity', 'picture', 'info')

admin.site.register(Item, ItemAdmin)
#
#
# class MyBugAdmin(admin.ModelAdmin):
#     list_display = ('customer', 'total_price')
#
# admin.site.register(MyBugAdmin, MyBag)

#
# class PurchaseAdmin(admin.ModelAdmin):
#     list_display = ('customer', 'buy_time', 'total_price')
#
# admin.site.register(PurchaseAdmin, Purchase)
