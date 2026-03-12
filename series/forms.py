from django import forms
from .models import Shot


class CSVImportForm(forms.Form):
    csv_file = forms.FileField(
        label="Select a CSV file", help_text="Upload a CSV file with shot data"
    )
    series = forms.ModelChoiceField(
        queryset=None,  # Will be set in view
        label="Series",
        required=True,
    )
    season_number = forms.IntegerField(
        label="Season Number", min_value=1, required=True
    )
    episode_number = forms.IntegerField(
        label="Episode Number", min_value=1, required=True
    )

    def __init__(self, *args, **kwargs):
        series_queryset = kwargs.pop("series_queryset", None)
        super().__init__(*args, **kwargs)
        if series_queryset is not None:
            self.fields["series"].queryset = series_queryset


class ShotForm(forms.ModelForm):
    """Form for creating and editing shots with image upload support."""
    
    class Meta:
        model = Shot
        fields = [
            "number", "script", "background", "camera_angle", 
            "camera_movement", "duration", "notes", "image"
        ]
        widgets = {
            "script": forms.Textarea(attrs={"rows": 4}),
            "notes": forms.Textarea(attrs={"rows": 3}),
            "background": forms.TextInput(attrs={"placeholder": "Describe the background"}),
            "camera_angle": forms.TextInput(attrs={"placeholder": "e.g., Wide shot, Close-up"}),
            "camera_movement": forms.TextInput(attrs={"placeholder": "e.g., Static, Pan, Dolly"}),
        }
