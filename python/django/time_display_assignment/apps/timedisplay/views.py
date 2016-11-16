from django.shortcuts import render, HttpResponse
import datetime

# Create your views here.
def index(request):
  
  now = datetime.datetime.now()

  context = {
    'now': now
  }

  return render(request, 'index.html', context=context)







# def yourMethodFromUrls(request):
#     context = {
#     "somekey":"somevalue"
#     }
#     return render(request,'appname/page.html', context)