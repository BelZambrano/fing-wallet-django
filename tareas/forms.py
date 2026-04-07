from django import forms
from .models import Transaccion, Usuario


class TransaccionForm(forms.ModelForm):
    class Meta:
        model = Transaccion
        fields = "__all__"


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = "__all__"
