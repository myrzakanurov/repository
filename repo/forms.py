from django import forms
from repo.models import Data


class RepoFileUploadForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ('title', 'description', 'data_file')
