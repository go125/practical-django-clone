from django import forms
from snippets.models import Snippet, Tag

class SnippetForm(forms.ModelForm):
    Tag_Select = forms.ModelMultipleChoiceField(
        queryset=Tag.objects,
        widget=forms.CheckboxSelectMultiple)  
    class Meta:
        model=Snippet
        fields=('title','code','description','Tag_Select')
