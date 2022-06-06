from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm

def registration(request):
    context = {
        'title': 'signup',
        'form': ''
    }

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        context['form'] = form
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created successfully, you can now login!')
            return redirect('login')
    else:
        form = UserRegistrationForm()
        context['form'] = form

    return render(request, 'users/register.html', context)

@login_required
def settings(request):
    return render(request, 'users/settings.html')