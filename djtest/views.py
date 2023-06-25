from django.http import HttpResponse
from django.core import management


def create_super_user():
    username = 'admin'
    email = 'admin@example.com'
    password = 'adminpassword'
    
    try:
        from django.contrib.auth.models import User

        User.objects.get(username=username)
        print('Superuser already exists.')
    except User.DoesNotExist:
        # Create the superuser
        management.call_command('createsuperuser', interactive=False, username=username, email=email)
        user = User.objects.get(username=username)
        user.set_password(password)
        user.save()
        print('Superuser created successfully.')



def index(request):
    management.call_command('check')
    management.call_command('collectstatic', verbosity=0, interactive=False)
    management.call_command('migrate', verbosity=0, interactive=False)
    create_super_user()
    
    return HttpResponse("Hello, world. You're at the polls index.")