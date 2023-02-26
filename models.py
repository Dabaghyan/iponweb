from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    registrated_at = models.DateTimeField(default=timezone.now)
    avatar = models.ImageField(upload_to="buyer/", blank=True, null=True)

# class Seller(models.Model):
# class Category:
#     objects = None

# StoreCategory
# Fields: name, picture


class StoreCategory(models.Model):
    name = models.OneToOneField(User, on_delete = models.CASCADE),
    picture = models.ImageField(upload_to="StoreCategory/", blank=True, null=True)
#
#
# # ItemCategory
# # FIelds:name, picture
#
#
class ItemCategory(models.Model):
    name = models.OneToOneField(User, on_delete = models.CASCADE),
    picture = models.ImageField(upload_to="StoreCategory/", blank=True, null=True)
#
#
# # Customer
# # Fields: user (ForeignKey to Django user), avatar(picture), registrated_at(when user registered)
#
#
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    registrated_at = models.DateTimeField(default=timezone.now)
    avatar = models.ImageField(upload_to="buyer/", blank=True, null=True)
#
#
# # StoreOwner
# # Fields: user (ForeignKey to Django user), avatar(picture), registrated_at(when user registered)
#
# class StoreOwner(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # registrated_at = models.DateTimeField(default=timezone.now)
    # avatar = models.ImageField(upload_to="buyer/", blank=True, null=True)
#
# # Store
# # Fields: name, owner (ForeignKey to StoreOwner), store_categroy (ForeignKey to StoreCategory)
#
#
# class Store(models.Model):
#     name = models.CharField(max_length=100)
#     owner = models.ForeignKey(StoreOwner, on_delete=models.CASCADE)
#     store_category = models.ForeignKey(StoreCategory, on_delete=models.CASCADE)
#
#
# # Item
# # Fields: name, picture, category (ForeignKey to ItemCategory), price, quantity, info, store(ForeignKey to Store)
#
#
class Item(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='item_pictures/', blank=True)
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    info = models.TextField(blank=True)
    # store = models.ForeignKey(Store, on_delete=models.CASCADE)
#
#
# # MyBag
# # Fields: customer (ForeignKey to Customer), items (ManyToMany to Item), total_price
#
#
# class MyBag(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     items = models.ManyToManyField(Item)
#     total_price = models.PositiveIntegerField(default=0)
# #
#
# # Purchase
# # Fields: items (ManyToMany to Item), buy_time, customer (ForeignKey to Customer), total_price.
#
# #
# class Purchase(models.Model):
#     items = models.ManyToManyField(Item)
#     buy_time = models.DateTimeField(default=timezone.now)
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     total_price = models.PositiveIntegerField(default=0)