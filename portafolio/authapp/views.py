from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.contrib import messages
from .forms import SignUpForm, ProfileForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('profile')
    else:
        form = SignUpForm()
    return render(request, 'authapp/registration/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'authapp/registration/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile_picture = form.cleaned_data.get('profile_picture')
            if profile_picture:
                profile = request.user.userprofile
                profile.profile_picture = profile_picture
                profile.save()
                messages.success(request, 'Imágen subida')
            else:
                messages.error(request, 'No se ha seleccionado ninguna imagen.')  # Agrega un mensaje de error si no se selecciona ninguna imagen
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.title()}: {error}")  # Agrega los errores del formulario como mensajes de error
    else:
        form = ProfileForm()
    return render(request, 'authapp/profile.html', {'form': form, 'messages': messages.get_messages(request)})

@login_required
def profileinfo(request):
    return render(request, 'authapp/profileinfo.html')