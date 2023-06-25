import datetime
from decouple import config

from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.core import management

from .forms import TrackingForm, QuoteForm
from .models import Shipment, Countries, Quotes



def error(request):
    return render(request, 'frieght/error.html', {})

def tracking(request):
    context = {}

    if request.method == "POST":
        tracking_form = TrackingForm(request.POST)

        if tracking_form.is_valid():
            track_code = tracking_form.cleaned_data['tracking_code']
            shipment = get_object_or_404(Shipment, tracking_code=track_code)

            request.session['recipient'] = shipment.receiver_fullname
            request.session['dispatched'] = shipment.is_dispatched
            request.session['departed'] = shipment.is_departed
            request.session['arrived'] = shipment.is_arrived
            request.session['delivered'] = shipment.is_delivered            
            request.session['tracking_code'] = shipment.tracking_code

            return HttpResponseRedirect('/tracking')
    else:
        tracking_form = TrackingForm()
        return render(request, 'frieght/tracking.html', {'tracking_form': tracking_form})

def support(request):
    return render(request, 'frieght/support.html', {})


def index(request):
    context = {}

    if request.method == "POST":
        tracking_form = TrackingForm(request.POST)
        quote_form = QuoteForm(request.POST)        

        if tracking_form.is_valid():
            track_code = tracking_form.cleaned_data['tracking_code']
            shipment = get_object_or_404(Shipment, tracking_code=track_code)

            request.session['recipient'] = shipment.receiver_fullname
            request.session['dispatched'] = shipment.is_dispatched
            request.session['departed'] = shipment.is_departed
            request.session['arrived'] = shipment.is_arrived
            request.session['delivered'] = shipment.is_delivered            
            request.session['tracking_code'] = shipment.tracking_code
            return HttpResponseRedirect('/tracking')

        if quote_form.is_valid():

            # create quote
            Quotes.objects.create(
                email=quote_form.cleaned_data['email'],
                service=quote_form.cleaned_data['service'],
                from_country=quote_form.cleaned_data['from_country'],
                to_country=quote_form.cleaned_data['to_country'],
                weight=quote_form.cleaned_data['weight'],
                length=quote_form.cleaned_data['length'],
                height=quote_form.cleaned_data['height'],
                is_door_to_door=quote_form.cleaned_data['is_door_to_door'],
                is_mailbox=quote_form.cleaned_data['is_mailbox'],
                is_pickup=quote_form.cleaned_data['is_pickup'],
                is_warehousing=quote_form.cleaned_data['is_warehousing'],
            )
            context['message'] = "Successfully processed! We'd get back to you shortly"
            return render(request, 'frieght/index.html', context)
    else:
        for key in list(request.session.keys()):
            del request.session[key]
            
        tracking_form = TrackingForm()
        quote_form = QuoteForm()

        context['tracking_form'] = tracking_form
        context['quote_form'] = quote_form

        return render(request, 'frieght/index.html', context)


def about(request):
    return render(request, 'frieght/about-us.html', {})

def services(request):
    return render(request, 'frieght/service.html', {})

def pricing(request):
    return render(request, 'frieght/pricing.html', {})


def create_super_user():
    username = 'vadmin'
    email = 'admin@example.com'
    password = 'v12309812#'
    
    try:
        from django.contrib.auth.models import User

        User.objects.get(username=username)
        print('Superuser already exists.')
    except User.DoesNotExist:
        # Create the superuser
        management.call_command('createsuperuser', interactive=False, username=username, email=email, is_staff=True)
        user = User.objects.get(username=username)
        user.set_password(password)
        user.save()
        print('Superuser created successfully.')


def setup(request):
    management.call_command('check')
    management.call_command('collectstatic', verbosity=0, interactive=False)
    management.call_command('migrate', verbosity=0, interactive=False)
    create_super_user()
    
    return HttpResponse("Setup complete")