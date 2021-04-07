from django import forms
from .models import Resume
gender = (('male','Male'),('female','Female'),('other','Other'))
job_city = (('delhi','Delhi'),('mumbai','Mumbai'),('bihar','Bihar'))

class ResumeForm(forms.ModelForm):
    gender  = forms.ChoiceField(choices=gender,widget=forms.RadioSelect())
    job_city = forms.MultipleChoiceField(choices=job_city,label='Preferrd city',widget=forms.CheckboxSelectMultiple())
    class Meta:
        model = Resume
        fields = ['name','dob','gender','locality','city','pin','state','mobile','email','job_city','profile_image','my_file']
        labels = {'name':'Full name','dob':'Date of Birth','gender':'Gender',
        'locality':'Locality','pin':'Pin Code','mobile':'Mobile Number','email':'Email ID',
        'profile_image':'Profile Image','my_file':'Document'}

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control'}),
            # 'gender':forms.TextInput(attrs={'class':'form-control'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'pin':forms.NumberInput(attrs={'class':'form-control'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'job_city':forms.TextInput(attrs={'class':'form-control'})}
        