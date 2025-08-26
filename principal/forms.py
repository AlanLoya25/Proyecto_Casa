from django import forms
from .models import Casa, Opinion, Promocion

class CasaForm(forms.ModelForm):
    class Meta:
        model = Casa
        exclude = ['propietario', 'fecha_creacion']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título de la casa'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
            'habitaciones': forms.NumberInput(attrs={'class': 'form-control'}),
            'banos': forms.NumberInput(attrs={'class': 'form-control'}),
            'metros_cuadrados': forms.NumberInput(attrs={'class': 'form-control'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'publicado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class OpinionForm(forms.ModelForm):
    mensaje = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 3, 
            'placeholder': 'Escribe tu opinión aquí...', 
            'class': 'form-control'
        }),
        label=''
    )

    class Meta:
        model = Opinion  
        fields = ['mensaje']
class PromocionForm(forms.ModelForm):
    class Meta:
        model = Promocion
        fields = ['titulo', 'descripcion', 'descuento', 'casa', 'fecha_inicio', 'fecha_fin']
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date'}),
        }
