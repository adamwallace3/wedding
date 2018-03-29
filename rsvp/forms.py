from django import forms
from .models import Rsvp


class Rsvp(forms.ModelForm):
    class Meta:
        model = Rsvp
        fields = ["name", "email", "phone_number", "guests", "comments"]

    # def __str__(self):
    #     return self.name
