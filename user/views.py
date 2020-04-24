from django.contrib import messages
from django.contrib.auth import logout, login, authenticate, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView
from user.models import UserProfile
from user.forms import SignUpForm, UserProfileForm, ChangePassword, MyAuthenticationForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            messages.success(request, f"Nowe konto założone: {username}")
            login(request, user)
            messages.info(request, f"Jesteś zalogowany/a jako {username}")
            return redirect('homepage')
    else:
        form = SignUpForm()
    return render(request, 'user/register.html', {'form': form})


def logout_request(request):
    logout(request)
    messages.info(request, "Wylogowano!")
    return redirect("homepage")


def login_request(request):
    if request.method == "POST":
        form = MyAuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Jesteś zalogowany/a jako {username}")
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                if 'login?next' in request.POST:
                    return redirect('homepage')
                else:
                    return redirect("homepage")
            else:
                messages.error(request, "Błędny login lub hasło")
        else:
            messages.error(request, "Błędny login lub hasło")
    form = MyAuthenticationForm()
    return render(request,
                  "user/login.html",
                  {"form": form})


class UserProfileView(UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    success_url = "/"
    template_name = "user/user_profile.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


def change_password(request):
    if request.method == 'POST':
        form = ChangePassword(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Hasło zostało zmienione!')
            return redirect('/')
        else:
            messages.error(request, 'Proszę poprawić błędy!')
    else:
        form = ChangePassword(request.user)
    return render(request, 'user/change_password.html', {'form': form})
