from django import forms


class Signupform(forms.Form):
    name = forms.CharField(max_length=20)
    email = forms.EmailField()
    verify_email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        verify_email = cleaned_data.get('verify_email')
        password = cleaned_data.get('password')

        if email != verify_email:
            raise forms.ValidationError('check your email')