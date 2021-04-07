from django.shortcuts import render
from .models import Resume
from .forms import ResumeForm
from django.views import View


# this Classbased view is used for get and post the data 
class ModelView(View):

    def get(self,request):
        form = ResumeForm()
        candidates = Resume.objects.all()

        return render(request,'myapp/resume.html',{'form':form,'candidates':candidates})
    
    # this method is for the post of the data through the above class
    def post(self,request):
        form = ResumeForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            form = ResumeForm()
        return render(request,'myapp/resume.html',{'form':form})

# this class is for the candidate whowing data
class Cnadndite(View):
    def get(self,request ,pk):
        candi = Resume.objects.get(pk=pk)
        return render(request,'myapp/candidate.html',{'candidate': candi})