from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['NameP']  # Chỉ định các trường mà người dùng có thể nhập liệu
