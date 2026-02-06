from django import forms
from .models import Supplier


class SupplierForm(forms.ModelForm):

    class Meta:
        model = Supplier
        fields = ('name', 'description')
        # Configurando os campos de form para o html
        widgets = {
            'name': forms.TextInput({'class': 'form-control'}),
            'description': forms.Textarea({'class': 'form-control', 'rows': 3})
        }
        labels= {
            'name': 'Nome',
            'description': 'Descrição'
        }
