from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, AuthenticationForm
from django.contrib.auth.models import User
from user.models import UserProfile
from django.utils.translation import ugettext_lazy as _


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='niewymagane', label='Imię')
    last_name = forms.CharField(max_length=30, required=False, help_text='niewymagane', label='Nazwisko')
    email = forms.EmailField(max_length=254, help_text='')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

        for fieldname in ['password1']:
            self.fields[fieldname].label = 'Hasło'

        for fieldname in ['password2']:
            self.fields[fieldname].label = 'Powtórz hasło'

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)
        labels = {
            'username': 'Nazwa użytkownika',
            'password1': 'hasło',
            'password2': 'powtórz hasło'
        }


class MyAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label="Nazwa użytkownika")
    password = forms.CharField(label="Hasło", widget=forms.PasswordInput)


class UserProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput, label='')
    about_me = forms.CharField(widget=forms.Textarea(attrs={"rows": 5, "cols": 20}), label="Napisz coś więcej o sobie")

    class Meta:
        model = UserProfile
        fields = ('avatar', 'about_me')


class ChangePassword(PasswordChangeForm):
    old_password = forms.CharField(
        label=_("Stare hasło"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus': True}),
    )
    new_password1 = forms.CharField(
        label=_("Nowe hasło"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text='',
    )
    new_password2 = forms.CharField(
        label=_("Powtórzone nowe hasło"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
