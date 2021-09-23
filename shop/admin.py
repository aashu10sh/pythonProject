from django.contrib import admin

# Register your models here.
from .models import Product, Deal, Shop

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_name", "price", "discount")
    list_display_links = ["product_name"]
    list_editable = ("price", "discount")
    search_fields = ("product_name", "price", "discount", "old_price")
    
class ShopAdmin(admin.ModelAdmin):
    list_display = ("shop_name", "contact", "location", "contact_person")
    list_display_links = ["shop_name"]
    list_editable = ("contact", "location", "contact_person")
    search_fields = ("shop_name", "contact", "location", "contact_person", "category", "email")
    
class DealAdmin(admin.ModelAdmin):
    list_display = ("deal_name", "valid_from", "valid_till", "discount_percent")
    list_display_links = ["deal_name"]
    list_editable = ("valid_from", "valid_till")
    search_fields = ("valid_from", "valid_till", "discount_percent")
    
admin.site.register(Product, ProductAdmin)
admin.site.register(Shop, ShopAdmin)
admin.site.register(Deal, DealAdmin)