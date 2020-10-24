from django import forms
from .models import Marriage


class Marriageform(forms.ModelForm):
    class Meta:
        model = Marriage
        fields = ['surname', 'first_name', 'other_names', 'gender', 'phone_number', 'phone_number_2', 'marital_status',
                  'date_of_birth', 'name', 'phone', 'email', 'gender_2', 'relationship']