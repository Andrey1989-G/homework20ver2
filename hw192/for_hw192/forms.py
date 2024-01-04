from django import forms

from for_hw192.models import Product, Version

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_product_name(self):
        ban_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево',
                    'бесплатно', 'обман', 'полиция', 'радар']
        cleaned_data = self.cleaned_data['product_name']
        for ban_word in ban_list:
            if ban_word in cleaned_data:
                raise forms.ValidationError('В названии имеются запрещенные продукты')

        return cleaned_data

    def clean_description(self):
        ban_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево',
                    'бесплатно', 'обман', 'полиция', 'радар']
        cleaned_data = self.cleaned_data['description']
        for ban_word in ban_list:
            if ban_word in cleaned_data:
                raise forms.ValidationError('В описании имеются запрещенные продукты')

        return cleaned_data

class VersionForm(forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'

