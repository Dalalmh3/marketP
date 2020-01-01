from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Submit
from django.core.validators import RegexValidator

from django import forms
from .models import Product

class ProductForm(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post' 
        
        self.helper.layout = Layout(
            'Product_Name_En','Product_Name_Ar','description','img_url',
            Submit('submit','create', css_class='btn-success')
        )
        
    class Meta:
        model = Product
        fields = ('Product_Name_En','Product_Name_Ar','description', 'img_url')


    
