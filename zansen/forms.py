from django import forms

class MessageForm(forms.Form):
    sender = forms.CharField(max_length=25, label='Nimimerkki')
    text = forms.CharField(widget=forms.widgets.Textarea(attrs={'rows':5, 'cols':75}), label='Viesti')
