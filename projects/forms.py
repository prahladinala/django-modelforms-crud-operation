# ALL MODEL FORMS ARE STORED HERE
from django.forms import ModelForm
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        # fields = ['title', 'description']
        # OR
        fields = '__all__'

# class MODELNAMEForm(ModelForm):
#     class Meta:
#         model = MODELNAME
#         # fields = ['title', 'description'] > creates form for specific fields mensioned here
#         # OR
#         fields = '__all__' > creates form for every available field in MODELNAME Class Provided > exception non editable fields(id) and automatic fields (created)

# TO USE THIS FORM WE NEED TO IMPORT IT INTO VIEWS AND USE IN createProject Class