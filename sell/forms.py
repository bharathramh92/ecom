from django import forms
from store.models import BookStore, Item, Author, Publisher
import autocomplete_light.shortcuts as autocomplete_light
from categories.category_helper import get_category_store_names

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        exclude = ['posting_datetime', 'last_updated_datetime']

class StoreSelectForm(forms.Form):
    store_name_choices = [(k, k) for k, v in get_category_store_names()['store_names'].items()]
    store_names = forms.ChoiceField(label= "Select a store", choices= store_name_choices)

class NewBookForm(forms.ModelForm):

    class Meta(ItemForm.Meta):
        model = BookStore
        exclude = ['item', 'authors', 'publisher']

class NewBookISBNCheckForm(forms.Form):

    isbn = forms.CharField(max_length= 13, min_length= 13, label= "ISBN", widget= forms.NumberInput())

    def clean_isbn(self):
        isbn = self.cleaned_data['isbn']
        try:
            int(isbn)
        except Exception:
            self.add_error('isbn', "ISBN should be a number")
        return isbn

class NewBookAuthorForm(autocomplete_light.ModelForm):
    class Meta:
        model = Author
        fields = ['name']
        labels = {'name': 'Author Name'}

class NewBookPublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name']
        labels = {'name': 'Publisher Name'}