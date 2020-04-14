from django import forms


class MapQueryForm(forms.Form):
    name = forms.CharField(max_length=255, required=True)
    origin = forms.CharField(max_length=45, required=True)
    origin_lat = forms.FloatField(required=True)
    origin_lng = forms.FloatField(required=True)
    destination = forms.CharField(max_length=45, required=True)
    destination_lat = forms.FloatField(required=True)
    destination_lng = forms.FloatField(required=True)
    polyline = forms.CharField(max_length=510, required=True)
    id = forms.IntegerField(required=False, widget=forms.HiddenInput())
    score = forms.FloatField(required=True)


class MarkProximityForm(forms.Form):
    difference = forms.DecimalField(decimal_places=2, required=True)
