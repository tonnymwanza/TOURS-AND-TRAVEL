from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib import messages

from . forms import ContactForm
from . models import Booking
from . models import Contact
from . models import Trending
from . forms import BookingForm
from . models import Rooms
# Create your views here.

class HomeView(View):

    def get(self, request):
        trending = Trending.objects.all()
        rooms = Rooms.objects.all()
        form = BookingForm(request.GET)
        context = {
            'form': form,
            'trending': trending,
            'rooms': rooms
        }
        return render(request, 'index.html', context)
    
    def post(self, request):
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = Booking.objects.create(
                destination = form.cleaned_data['destination'],
                check_in = form.cleaned_data['check_in'],
                check_out = form.cleaned_data['check_out'],
                adults = form.cleaned_data['adults'],
                children = form.cleaned_data['children']
            )
            form = BookingForm()
            messages.info(request, 'thank you. booking completed')
        else:
            messages.error(request, 'error encountered during booking')
        
        context = {
            'form': form
        }
        return render(request, 'index.html', context)
    

class AboutView(View):

    def get(self, request):
        return render(request, 'about.html')
    

class ContactView(View):

    def get(self, request):
        form = ContactForm(request.GET)
        context = {
            'form': form
        }
        return render(request, 'contact.html', context)
    
    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = Contact.objects.create(
                name = form.cleaned_data['name'],
                email = form.cleaned_data['email'],
                subject = form.cleaned_data['subject'],
                message = form.cleaned_data['message']
            )
            form = ContactForm()
            messages.success(request, 'Info send successfully')
        else:
            messages.error(request, 'error encountered while sending message!!')
        context = {
            'form': form
        }
        return render(request, 'contact.html', context)
    
class OfferView(View):
    
    def get(self, request):
        return render(request, 'offers.html')
    

def register_user(request): # function view to register a user
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'the username is in use. choose another one')
                return redirect('register_user')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'the email is in use, choose another one')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                return redirect('login_user')
        else:
            messages.error(request, 'check the passwords. they dont match')
            return redirect('register_user')
    return render(request, 'register.html')

def login_user(request): # function view to login a user
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST[next])
            else:
                return redirect('home')
        else:
            messages.info(request, 'invalid username or password')
            return redirect('login_user')
    return render(request, 'login.html')