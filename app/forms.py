from django import forms

class Paragraph(forms.Form):
    Text = forms.CharField(widget = forms.Textarea)

class UploadFileForm(forms.Form):
	Upload = forms.FileField()    