from django import forms
class contactform(forms.Form):
    name=forms.CharField()
    age=forms.IntegerField()
    password=forms.CharField(widget=forms.PasswordInput)
    gender=forms.ChoiceField(choices=(['male','MALE'],['female','FEMALE']),widget=forms.RadioSelect)
   # course=forms.MultipleChoiceField(choices=(['python','PYTHON'],['django','DJANGO']))
    #course=forms.MultipleChoiceField(choices=(['python','PYTHON'],['django','DJANGO']),widget=forms.RadioSelect)