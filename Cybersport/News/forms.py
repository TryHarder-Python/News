from django import forms
from .models import Category


class NewsForm(forms.Form):
    title = forms.CharField(max_length=200)
    text = forms.Textarea()
    is_published = forms.BooleanField()
    category = forms.ModelChoiceField(queryset=Category.objects.all())
