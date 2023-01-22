from django.shortcuts import render
from django.http import HttpResponse
from .forms import TestForm
from app.functions import handle_uploaded_file  
from app.functions import *
from app.functions import send_email
from django.core.files.storage import default_storage

# Create your views here.

def index(request):
    if request.method == 'POST':  
        form = TestForm(request.POST, request.FILES)  
        handle_uploaded_file(request.FILES['file'])  
        file = request.FILES['file']
        if form.is_valid():   
            weights = form.cleaned_data.get("weights")
            impacts = form.cleaned_data.get("impacts")
            email = form.cleaned_data.get("email")
            topsis(weights, impacts, file.name) 
            send_email(email)
            default_storage.delete('static/app/datasets/output.csv')
        else:
            print(form.errors)
        default_storage.delete('static/app/datasets/'+file.name)
        return render(request,"app/index.html",{'form':form})

    form = TestForm() 
    return render(request,"app/index.html",{'form':form})  