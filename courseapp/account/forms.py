from django.contrib.auth.forms import AuthenticationForm
from django.forms import widgets
from django.contrib import messages
from courses import forms

class LoginUserForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget = widgets.TextInput(attrs={"class": "form-control"})
        self.fields["password"].widget = widgets.PasswordInput(attrs={"class": "form-control"})
    
    def clean_username(self):
        username = self.cleaned_data.get("username")

        if username == "admin":
            messages.add_message(self.request, messages.SUCCESS, "Welcome Admin")

        return username
    
    def confirm_login_allowed(self, user):
        if user.username.startswith("x"):
            raise forms.ValidationError("You cannot log in with this username")
        