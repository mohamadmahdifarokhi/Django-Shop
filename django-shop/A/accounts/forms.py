from django import forms
from .models import User, OtpCode
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField


# formy ke dakhel admin panel estefade mikonim
class UserCreationForm(forms.ModelForm):
    p1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    p2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'phone_number', 'full_name')

    def clean_p2(self):
        cd = self.cleaned_data
        if cd['p1'] and cd['p2'] and cd['p1'] != cd['p2']:
            raise ValidationError('Passwords don\'t match.')
        return cd['p2']

    # commit az samt code dare bara ma miad
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['p1'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        help_text="Raw passwords are not stored, so there is no way to see this user\'s password, but you can change "
                  "the password using <a href=\"../password/\">this form</a>.")

    class Meta:
        model = User
        fields = ('email', 'phone_number', 'full_name', 'password', 'last_login')


class UserRegisterationForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': 'w-25'}))
    full_name = forms.CharField(label='Full name', widget=forms.TextInput(attrs={'class': 'w-25'}))
    phone_number = forms.CharField(label='Phone number', max_length=11, widget=forms.TextInput(attrs={'class': 'w-25'}))
    # widget = forms.PasswordInput ==> *****
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'w-25'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()
        if user:
            raise ValidationError('This email is already taken.')
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        user = User.objects.filter(phone_number=phone_number).exists()
        if user:
            raise ValidationError('This phone number is already taken.')
        OtpCode.objects.filter(phone_number=phone_number).delete()
        return phone_number


class VerifyCodeForm(forms.Form):
    code = forms.IntegerField()


class UserLoginForm(forms.Form):
    phone_number = forms.CharField(label='Phone number', max_length=11, widget=forms.TextInput(attrs={'class': 'w-25'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'w-25'}))