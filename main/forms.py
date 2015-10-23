from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, HTML, Layout, Div
from crispy_forms.bootstrap import FormActions
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from main.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        # del self.fields['username']

    class Meta:
        model = CustomUser
        fields = ("email",)
        exclude = ['username']


class CustomUserChangeForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(CutomUserChangeForm, self).__init__(*args, **kwargs)
        # del self.fields['username']

    class Meta:
        model = CustomUser
        fields = ["email", "password"]
        exclude = ['username']


class UserSignUp(forms.Form):
    email = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())
    name = forms.CharField(required=True)


class UserLogin(forms.Form):
    email = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())


class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    message = forms.CharField(required=True, widget=forms.Textarea)

    # args are variables, kew-word arguments are variables and a value
    # val ,   val2="something"
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = '/contact_view/'
        self.helper.layout = Layout(
                Div('name', 'email', 'phone', css_class='col-md-6'),
                Div('message', css_class='col-md-6')
            )

        self.helper.layout.append(
            FormActions(
                Submit('submit', 'Submit', css_class="btn-primary")
                )
            )