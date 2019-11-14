from django.shortcuts import render
from . import forms
from basicApp.forms import newUser

# Create your views here.
def index(request):
    return render(request, 'basicApp/index.html')

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("Validation success.")
            print('Name: ' + form.cleaned_data['name'])
            print('Email: ' + form.cleaned_data['email'])
            print('Text: ' + form.cleaned_data['text'])

    return render(request, 'basicApp/forms.html', {'form':form})

def users(request):
    form = newUser()
    if request.method == "POST":
        form = newUser(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Bad Form")

    return render(request, 'basicApp/users.html', {'form':form})
