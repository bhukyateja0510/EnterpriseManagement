from django.shortcuts import render
from django.contrib import messages
from .forms import UserRegistrationForm

# Create your views here.
def home(request):
    return render(request,'index.html')

#UserRegisterActions
def UserRegister(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print('Data is Valid')
            form.save()
            messages.success(request, 'You have been successfully registered')
            form = UserRegistrationForm()
            return render(request, 'userregistration.html', {'form': form})
        else:
            messages.success(request, 'Email or Mobile Already Existed')
            print("Invalid form")
    else:
        form = UserRegistrationForm()
    return render(request, 'userregistration.html', {'form': form})