from django import forms


class ContactForm(forms.Form):

    fullname = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'placeholder':'Full Name',
        'class': 'form-control',
      
        
        
    }))
    message = forms.CharField(required=False,widget=forms.Textarea(attrs={
        'rows': '7',
        'class': 'form-control',
        'placeholder': 'Input Message',
        'name':'message' ,
        'id':'message' ,
        'cols':'30' 
    }))
    subject = name = forms.CharField( required=False,widget=forms.TextInput(attrs={
        'placeholder': 'subject',
        'class': 'form-control',
        'name':'subject',
    }
        ))
    email = forms.EmailField(required=False,widget=forms.TextInput(attrs={
        'placeholder': 'email',
        'class': 'form-control',
        'name':'email',
    }
        ))