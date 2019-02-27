from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect





def sign_in(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('/')
        else:
            print(form.errors)

    return render(request, 'account/sign_in.html', {'form': form})


def sign_out(request):
    logout(request)
    return redirect(reverse('account:sign_in'))




def sign_up(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('account:sign_in'))
        else:
            print(form.errors)
    return render(request, 'account/sign_up.html', {'form': form})
    # return render(request, 'account/sign_up.html', {})