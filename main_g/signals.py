from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import SalesRecord

@receiver(post_save, sender=SalesRecord)
def update_inventory(sender, instance, created, **kwargs):
    if created:
        item = instance.item
        item.quantity -= instance.quantity_sold
        item.save()