from django import forms
from django.forms import NumberInput
from .models import Product


class ProductCreateForm(forms.ModelForm):
    # name = forms.CharField(widget=forms.TextInput)
    # description = forms.CharField(widget=forms.TextInput)
    # price = forms.IntegerField(min_value=1, widget=forms.NumberInput)
    # quantity = forms.IntegerField(widget=NumberInput)
    # image = forms.FileField(widget=forms.FileInput)
    # is_published = forms.BooleanField(widget=forms.CheckboxInput)
    # delivery_time = forms.IntegerField(widget=forms.NumberInput)

    class Meta:
        model = Product
        fields = ('name','description','price','quantity','is_published','category','delivery_time','brand')

