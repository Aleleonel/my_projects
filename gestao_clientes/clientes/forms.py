from django.forms import ModelForm
from .models import Person, Sales

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'age', 'doc', 'salary', 'bio', 'photo']
