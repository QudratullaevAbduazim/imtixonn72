from django import forms
from .models import Phones
class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phones
        fields = '__all__'

    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise forms.ValidationError('Narxni togri kiriting!')
        return price

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 2:
            raise forms.ValidationError('Xatolik Iltimos belgilar 2 ta xarfdan kop bolsin!')
        return name

    def clean_amount(self):
        amount = self.cleaned_data['amount']
        if amount <= 0:
            raise forms.ValidationError('Manfiy son mumkun emas!')
        return amount

    def clean_year(self):
        year = self.cleaned_data['year']
        if year > 2025:
            raise forms.ValidationError('Yilni togri kiriting!')
        return year






