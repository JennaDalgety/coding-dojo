from django.shortcuts import render, redirect
from .models import User

# Create your views here.


def index(request):

  return render(request, 'login_register_app/index.html')


def process(request):
  print 'we are in the process method!'
  if request.method == 'POST':
    print request.POST

    User.objects.create_user(request.POST)

   

  return redirect(index)