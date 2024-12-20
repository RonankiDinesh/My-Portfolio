from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from .forms import UserRegisterForm

# Index view
def index(request):
    return render(request, 'user/index.html', {'title': 'Index'})

# Register view
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')

            # Send welcome email
            htmly = get_template('user/Email.html')
            context = {'username': username}
            subject = 'Welcome!'
            from_email = 'dineshronanki777@gmail.com'
            to_email = [email]
            html_content = htmly.render(context)
            msg = EmailMultiAlternatives(subject, html_content, from_email, to_email)
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            # Display success message and redirect
            messages.success(request, f'Your account has been created! You are now able to log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()  # Render an empty form for GET requests
    
    return render(request, 'user/register.html', {'form': form, 'title': 'Register Here'})

# Login view
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)  # Use `auth_login` to avoid shadowing the `login` function
                messages.success(request, f'Welcome, {username}!')
                return redirect('index')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid form submission.')

    else:
        form = AuthenticationForm()  # Empty form for GET requests
    
    return render(request, 'user/login.html', {'form': form, 'title': 'Log In'})
