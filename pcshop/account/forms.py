from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import PasswordInput, TextInput

User = get_user_model()

class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        self.fields['email'].label = 'Ваша e-mail адреса'
        self.fields['email'].required = True
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''

    def clean_email(self):
        email = self.cleaned_data.get('email').lower()
        if User.objects.filter(email=email).exists() and len(email) > 254:
            raise forms.ValidationError("Така e-mail адреса вже зареєстрована або завелика")
        return email
    
class UserLoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget = TextInput(attrs={'placeholder': 'Ваш логін'})
        self.fields['password'].widget = PasswordInput(attrs={'placeholder': 'Ваш пароль'})

        