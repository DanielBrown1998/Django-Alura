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
                'autocomplete': 'off'
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
                'type': 'password',

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
                'autocomplete': 'off'
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
                'autocomplete': 'off'
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
                'type': 'password',
            },
        ),
        help_text= [
            'A senha deve conter no mínimo 8 caracteres',
            'A senha não pode ser muito comum',
            'A senha não pode ser inteiramente numérica',
        ]
    )
    confirmar_senha = forms.CharField(
        label="Confirmar Senha",
        required=True,
        max_length=20,
        widget= forms.PasswordInput(
            attrs={
                'placeholder': 'Confirme sua senha',
                'class': 'form-control',
                'type': 'password',
            },
        ),
        help_text= [
            'Digite a mesma senha do campo anterior',
        ]
    )
    def clean(self):
        cleaned_data = self.cleaned_data
        senha = cleaned_data.get('senha')
        confirmar_senha = cleaned_data.get('confirmar_senha')
        if senha != confirmar_senha:
            msg = forms.ValidationError('As senhas não conferem', code='invalid')
            self.add_error('confirmar_senha', msg)
        return super().clean()