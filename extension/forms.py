from django import forms
from django.forms import ModelForm


from django.shortcuts import render
from django.http import HttpResponseRedirect

SEARCH_OPTIONS = (
    ('playlist'),
    ('album'),
    ('artist'),
)


class SearchForm(forms.ModelForm):
    error_css_class = 'error'
    option = forms.CharField(label='What is your favorite fruit?', widget=forms.Select(choices=SEARCH_OPTIONS))

    # forms.ChoiceField(choices=SEARCH_OPTIONS, required=True )
    class Meta:

        fields = ['option']




class StartForm(forms.Form):
    option = forms.CharField(max_length=10)
    name = forms.CharField(max_length=20)

class ResultForm(forms.Form):
    btn = forms.CharField()

def search(self, request):
    submitted = False
    if request.method == 'POST':
        form = StartForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        # assert False
        return HttpResponseRedirect('/SearchOptions?submitted=True')
    else:
        form = StartForm()
    if 'submitted' in request.GET:
        submitted = True

    return render(request, 'results.html', {'form': form, 'submitted': submitted})
