from django import forms

class LoginForm(forms.Form):
    nome_login = forms.CharField(
        label="Nome de Login",
        required=True,
        max_length=100,
        widget= forms.TextInput(
            attrs={
                'placeholder': 'Digite seu nome de login',
                'class': 'form-control',
            },
        ),
    )
    senha = forms.CharField(
        label="Senha",
        required=True,
        max_length=20,
        widget= forms.PasswordInput(
            attrs={
                'placeholder': 'Digite sua senha',
                'class': 'form-control',

            },
        ),
    )

class CadastroForm(forms.Form):
    nome = forms.CharField(
        label="Nome",
        required=True,
        max_length=100,
        widget= forms.TextInput(
            attrs={
                'placeholder': 'Digite seu nome',
                'class': 'form-control',
            },
        ),
    )
    email = forms.EmailField(
        label="Email",
        required=True,
        widget= forms.EmailInput(
            attrs={
                'placeholder': 'Digite seu email',
                'class': 'form-control',
            },
        ),
    )
    senha = forms.CharField(
        label="Senha",
        required=True,
        max_length=20,
        widget= forms.PasswordInput(
            attrs={
                'placeholder': 'Digite sua senha',
                'class': 'form-control',
            },
        ),
    )
    confirmar_senha = forms.CharField(
        label="Confirmar Senha",
        required=True,
        max_length=20,
        widget= forms.PasswordInput(
            attrs={
                'placeholder': 'Confirme sua senha',
                'class': 'form-control',
            },
        ),
    )
    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get('senha')
        confirmar_senha = cleaned_data.get('confirmar_senha')
        if senha != confirmar_senha:
            raise forms.ValidationError('As senhas não conferem')
        return cleaned_data
