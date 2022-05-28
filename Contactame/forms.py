from django import forms

class Formulario_contacto(forms.Form):
    nombre = forms.CharField(label="", max_length=60, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Nombre', 'style': 'background: transparent; color:white; border-radius: 10px; border-width: 2px;'}))
    email = forms.EmailField(label="", required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Email','style': 'color:white; background: transparent; border-radius:10px; border-width: 2px;'}))
    contenido = forms.CharField(label="", required=True, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Contenido del mensaje','style': 'color:white; background: transparent; border-radius: 10px;border-width: 2px;'}))