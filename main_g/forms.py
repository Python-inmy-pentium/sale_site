from django import forms
from .models import SalesRecord, InventoryList


class SalesRecordForm(forms.ModelForm):
    class Meta:
        model = SalesRecord
        fields = ['item', 'quantity_sold']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        super().__init__(*args, **kwargs)
        self.fields["item"].queryset = InventoryList.objects.filter(user=user)

    def clean(self):
        cleaned_data = super().clean()
        item = cleaned_data.get('item')
        quantity_sold = cleaned_data.get('quantity_sold')

        if item and quantity_sold and item.quantity < quantity_sold:
            raise forms.ValidationError("Not enough stock available.")
        return cleaned_data