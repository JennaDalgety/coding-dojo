from django.shortcuts import render, redirect
#CONTROLLER!
# Create your views here.
def index(request):
  return render(request, 'first_app/index.html')


def show(request):
  return render(request, 'first_app/show_users.html')

def create(request):
  print (request.method)
  if request.method =='POST':
    print (request.POST)
  else:
    return redirect('/')
