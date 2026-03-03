from django import forms


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
