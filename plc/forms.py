from django import forms
from plc.models import ProductList, PriceList, OutputCsv

class CreateProductListForm(forms.ModelForm):
    class Meta:
        model = ProductList
        fields = ['title', 'file']

class CreatePriceListForm(forms.ModelForm):
    class Meta:
        model = PriceList
        fields = ['title', 'file']


class CreateOutputCsvForm(forms.ModelForm):
    class Meta:
        model = OutputCsv
        fields = ['title', 'product_list', 'price_list', 'product_list_search_field', 'product_list_replace_field', 'price_list_search_field', 'price_list_replace_field']
        widgets = { 'product_list_search_field': forms.Select(), 'product_list_replace_field': forms.Select(), 'price_list_search_field': forms.Select(), 'price_list_replace_field': forms.Select(),}