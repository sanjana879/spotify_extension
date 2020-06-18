from django import forms

from extension.models import SearchOptions
SEARCH_OPTIONS = (
    ('playlist'),
    ('album'),
    ('artist'),
)

class SearchForm(forms.ModelForm):
    error_css_class = 'error'
    option = forms.CharField(label='What is your favorite fruit?', widget=forms.Select(choices=SEARCH_OPTIONS))
        #forms.ChoiceField(choices=SEARCH_OPTIONS, required=True )
    class Meta:
        model = SearchOptions
        fields = ['option']