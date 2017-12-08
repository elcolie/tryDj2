from django import forms

from openingstocks.models import OpeningStock


class OpeningStockForm(forms.ModelForm):
    quantity = forms.IntegerField(disabled=True)

    class Meta:
        model = OpeningStock
        fields = [
            'miti',
            'item_group',
            'item',
            'quantity',
            'value',
            'specification',
        ]
