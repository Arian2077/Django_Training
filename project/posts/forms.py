from django import forms

class Postform(forms.Form):
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)
    is_enable = forms.BooleanField()
    publish_field = forms.DateTimeField()
