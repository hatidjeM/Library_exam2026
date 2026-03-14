from django import forms
from .models import Book

class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

    def clean_published_year(self):
        year = self.cleaned_data['published_year']
        if year < 1900:
            raise forms.ValidationError("Year must be after 1900")
        return year

class BookEditForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ['author']  # пример за exclude field