from django import forms

class ContactForm(forms.Form):

    name = forms.CharField(label="Nombre",required=True, widget=forms.TextInput(
        attrs={'class':'form-control ml-2', 'placeholder':'Nombre y Apellido'}
    ), min_length=3, max_length=100)
    email = forms.EmailField(label="Email",required=True, widget=forms.EmailInput(
        attrs={'class':'form-control ml-1', 'placeholder':"Email"}
    ), min_length=3, max_length=100)
    content = forms.CharField(label="Mensaje", required=True, widget=forms.Textarea(
        attrs={'class':'form-control ml-1', 'rows': 5, 'placeholder':"Mensaje"}
    ), min_length=10, max_length=1000)