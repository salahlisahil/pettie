from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Pettie
from django.contrib.auth.hashers import check_password
from .forms import PettieSignUpForm
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib import messages
from django.urls import reverse


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def events(request):
    return render(request, "events.html")


def ourteam(request):
    return render(request, "ourteam.html")


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = Pettie.objects.filter(email=email).first()
        if user:
            if check_password(password, user.password):
                # Password matches, successful login
                messages.success(request, f'Welcome {email.split("@")[0].strip()}')
            else:
                messages.error(request, 'Email or password is incorrect')
        else:
            messages.error(request, 'Email or password is incorrect')

        # try:
        #     user = Pettie.objects.get(email=email)
        #     if check_password(password, user.password):
        #         # Password matches, successful login
        #         messages.success(request, f'Welcome {email.split("@")[0].strip()}')
        #     else:
        #         # Password does not match
        #         messages.error(request, 'Login failed. Please, <a href="#">update password</a>')
        # except Pettie.DoesNotExist:
        #     # Email not found
        #     messages.error(request, 'Email not found.')

        return render(request, 'login.html', {'messages': messages.get_messages(request)})

    return render(request, 'login.html', {'messages': messages.get_messages(request)})


def signup(request):
    success_message = None

    if request.method == 'POST':
        form = PettieSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
            # success_message = "You registered successfully!"
    else:
        form = PettieSignUpForm()

    return render(request, 'signup.html', {'form': form, 'success_message': success_message, 'errors': form.errors})


def recover_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        user = Pettie.objects.filter(email=email).first()
        if not user:
            messages.error(request, f'This email not found')
            return redirect('recover_password')

        subject = 'Email for password recovering'
        message = 'Here is the message.'
        email_from = 'sender@example.com'
        recipient_list = [user.email, ]

        send_mail(subject, message, email_from, recipient_list)

        messages.success(request, f'Email was send to your address')
        return redirect('recover_password')

    return render(request, 'reset_pwd.html')


def contact_us(request):
    message = request.POST.get('contact-text')
    if message:
        subject = 'Email from contact us form'
        email_from = 'Also your email here'
        recipient_list = ['Your email here', ]

        send_mail(subject, message, email_from, recipient_list)

    return HttpResponse('200')
