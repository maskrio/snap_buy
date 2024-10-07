from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags
class ProductEntryForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "price"]
    def clean_product(self):
        product = self.cleaned_data["product"]
        return strip_tags(product)

    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)