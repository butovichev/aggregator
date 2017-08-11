from django import forms
from django.contrib.auth.models import User


USER_ROLE_CHOICES = (
    ('gamer', ("Игрок")),
    ('partner', ("Партнер")),

)


class UserForm(forms.ModelForm):
    user_type = forms.ChoiceField(choices=USER_ROLE_CHOICES, label="Регистрация", initial='',
                                  widget=forms.Select(), required=True)
    username = forms.CharField(max_length=30)
    firstname = forms.CharField(max_length=30, required=False)
    lastname = forms.CharField(max_length=30, required=False)
    phone = forms.CharField(max_length=30, required=False)
    email = forms.CharField(max_length=30)
    pass1 = forms.CharField(widget=forms.PasswordInput, label="Пароль",
                            min_length=6, max_length=30)
    pass2 = forms.CharField(widget=forms.PasswordInput, label="Пароль ещё раз")

    def clean_pass2(self):
        if (self.cleaned_data["pass2"] != self.cleaned_data.get("pass1", "")):
            raise forms.ValidationError("Пароли не совпадают")
        return self.cleaned_data["pass2"]

    class Meta:
        model = User
        fields = ('user_type',)
