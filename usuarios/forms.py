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
        error_messages=[],
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
        error_messages=[],
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
        ],
        error_messages=[],
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
        ],
        error_messages=[],
    )

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if not nome:
            msg = forms.ValidationError('Nome é um campo obrigatório', code='invalid')
            self.add_error('nome', msg)
        if " " in nome.strip():
            msg = forms.ValidationError('Nome não pode conter espaços', code='invalid')
            self.add_error('nome', msg)
        if len(nome) < 3:
            msg = forms.ValidationError('Nome muito curto', code='invalid')
            self.add_error('nome', msg)
        return nome

    def clean(self):
        cleaned_data = self.cleaned_data
        senha = cleaned_data.get('senha')
        confirmar_senha = cleaned_data.get('confirmar_senha')
        if senha != confirmar_senha:
            msg = forms.ValidationError('As senhas não conferem', code='invalid')
            self.add_error('confirmar_senha', msg)
        return super().clean()