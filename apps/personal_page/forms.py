from django import forms

from apps.personal_page import models

class PersonForm(forms.models.ModelForm):

    class Meta:
        model = models.Person


