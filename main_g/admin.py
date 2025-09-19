from django.contrib import admin
from .models import InventoryList, SalesRecord
# Register your models here.
admin.site.register(InventoryList)
admin.site.register(SalesRecord)