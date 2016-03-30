from django import forms

class Paragraph(forms.Form):
    Text = forms.CharField(widget = forms.Textarea)