
from django import forms


class SendCommentForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput())
    fio = forms.CharField(widget=forms.TextInput())
    number = forms.IntegerField(widget=forms.NumberInput())
    nameProject = forms.CharField(widget=forms.TextInput())
    pasport = forms.ImageField()
    comment = forms.CharField(widget=forms.TextInput())
    sphere = forms.CharField(widget=forms.TextInput())
    sum = forms.IntegerField(widget=forms.NumberInput())
    payback = forms.IntegerField(widget=forms.NumberInput())
    Yield = forms.IntegerField(widget=forms.NumberInput())
    address = forms.CharField(widget=forms.TextInput())
    actualPlace = forms.CharField(widget=forms.TextInput())
    document = forms.CharField(widget=forms.TextInput())
    assets = forms.CharField(widget=forms.TextInput())
    contribution = forms.CharField(widget=forms.TextInput())
    date = forms.DateTimeField(widget=forms.DateInput())
    comment2 = forms.CharField(widget=forms.TextInput())