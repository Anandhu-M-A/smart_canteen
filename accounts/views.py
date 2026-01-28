from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth import login

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('signup')
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})

