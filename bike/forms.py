from django import forms


class MapQueryForm(forms.Form):
    id = forms.IntegerField(required=False, widget=forms.HiddenInput())
    origin = forms.CharField(max_length=45, required=True)
    origin_lat = forms.FloatField(required=True)
    origin_lng = forms.FloatField(required=True)
    destination = forms.CharField(max_length=45, required=True)
    destination_lat = forms.FloatField(required=True)
    destination_lng = forms.FloatField(required=True)
    polyline = forms.CharField(max_length=510, required=True)
    score = forms.FloatField(required=True),
    name = forms.CharField(max_length=255, required=True)
