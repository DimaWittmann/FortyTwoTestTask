from django import forms


from apps.personal_page import models
from apps.personal_page.widgets import ImageWidget


class PersonForm(forms.models.ModelForm):

    class Meta:
        model = models.Person

        widgets = {
            'image': ImageWidget(),
            'date_of_birth': forms.widgets.DateInput(
                attrs={'autocomplete': 'off'}
            ),
        }
