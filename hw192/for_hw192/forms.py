from django import forms

from for_hw192.models import Product, Version

class ProductForm(forms.ModelForm):
    ban_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево',
                'бесплатно', 'обман', 'полиция', 'радар']
    class Meta:
        model = Product
        fields = '__all__'

    def clean_product_name(self):
        cleaned_data = self.cleaned_data['product_name']
        for ban_word in self.ban_list:
            if ban_word in cleaned_data:
                raise forms.ValidationError('В названии имеются запрещенные продукты')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        for ban_word in self.ban_list:
            if ban_word in cleaned_data:
                raise forms.ValidationError('В описании имеются запрещенные продукты')

        return cleaned_data

class VersionForm(forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'

class ProductFormUser(ProductForm):
    class Meta:
        model = Product
        fields = ('product_name', 'descriptions', 'image', 'category', 'price')

class ProductFormModerator(ProductForm):
    class Meta:
        model = Product
        fields = ('descriptions', 'category', 'is_published')
