from allauth.account.forms import LoginForm, forms


class MyLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(MyLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget = forms.TextInput(
            attrs={'type': 'text', 'class': 'input'})
        self.fields['password'].widget = forms.PasswordInput(
            attrs={'class': 'input'})
