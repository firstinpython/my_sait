from django import forms
from django.utils.safestring import mark_safe

class CustomOrderingWidget(forms.Select):
    def __init__(self, attrs=None, choices=()):
        super().__init__(attrs, choices)
        self.choices = choices

    def render(self, name, value, attrs=None, renderer=None):
        output = super().render(name, value, attrs, renderer)
        return mark_safe(output)

    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option = super().create_option(name, value, label, selected, index, subindex, attrs)
        if value == 'price':
            option['label'] = "ты ебать бомж"
        elif value == '-price':
            option['label'] = "мажор ебаный"
        return option