from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from user.models import UserProfile


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

# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         # fields = ('avatar',)
#         # labels = {'avatar': 'Awatar'}
