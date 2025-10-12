from django import forms
from .models import Video

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ["MovieTitle", "Actor1Name", "Actor2Name", "DirectorName", "MovieGenre", "ReleaseYear"]
        widgets = {
            "MovieTitle": forms.TextInput(attrs={"class": "input", "placeholder": "e.g., Inception"}),
            "Actor1Name": forms.TextInput(attrs={"class": "input", "placeholder": "Lead actor"}),
            "Actor2Name": forms.TextInput(attrs={"class": "input", "placeholder": "Supporting actor"}),
            "DirectorName": forms.TextInput(attrs={"class": "input", "placeholder": "Director"}),
            "MovieGenre": forms.Select(attrs={"class": "select"}),
            "ReleaseYear": forms.NumberInput(attrs={"class": "input", "min": 1888}),
        }

