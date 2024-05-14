from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import UserRegistrationForm


# Create your views here.

@login_required
def index(request):
    return render(request, 'dashboard.html')


def register(request):
    form = UserRegistrationForm()

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()

            return render(request, 'account/register_done.html', {'new_user': new_user})

    return render(request, "account/register.html", {'form': form})

