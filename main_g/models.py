from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User
from django.utils.timezone import now


# Create your models here.


class InventoryList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name}, {self.price}, {self.quantity}"


class SalesRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    sale_id = models.CharField(max_length=20, unique=True, blank=True)
    item = models.ForeignKey(InventoryList, on_delete=models.CASCADE)
    quantity_sold = models.PositiveIntegerField()
    sale_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.sale_id:
            today = now().date()
            date_str = today.strftime("%Y-%m%d")

            # Count how many sales already exist for today
            count_today = SalesRecord.objects.filter(sale_date__date=today).count() + 1
            self.sale_id = f"{date_str}-{count_today:04d}"

        super().save(*args, **kwargs)

    def total_sale_amount(self):
        return self.item.price * self.quantity_sold

    def __str__(self):
        return f"{self.quantity_sold} x {self.item.price} on {self.sale_date}"