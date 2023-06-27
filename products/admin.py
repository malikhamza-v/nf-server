from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple
from .models import Product, Category, AvailableColors, AvailableSizes, ProductImages
from knox.models import AuthToken
from django.contrib.auth.models import Group, User


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name", )}
    list_display = ("name", "original_price", "is_at_discount", "discounted_percent")
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

class AvailableColorsAdmin(admin.ModelAdmin):
    list_display = ("name", "hex_code")


class ProductImagesAdmin(admin.ModelAdmin):
    list_display = ('product', "image")
    ordering = ("product", )

class UserAdmin(admin.ModelAdmin):
    exclude = ("groups", "user_permissions")

admin.site.register(ProductImages, ProductImagesAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(AvailableColors, AvailableColorsAdmin)
admin.site.register(AvailableSizes)
admin.site.unregister(AuthToken)
admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)