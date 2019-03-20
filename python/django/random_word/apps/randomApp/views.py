from django.shortcuts import render, HttpResponse
import random
import string

# Create your views here.

def index(request):

  return render(request, 'random_app/index.html')


# def choice(enum):    # this function is what the .choice function below does/is

#   return enum[random.randint(0, len(enum))]


def generate(request):
  print 'we are in the generate function!'

  random_word = ''.join([random.choice(string.letters + string.digits) for n in range(14)])
  
  try:
     request.session['count']  # pass count in as .session here because it needs to track the counts for the duration of the user's stay
  except KeyError:
     request.session['count'] = 0
  request.session['count'] += 1
  print request.session['count']

  context = {
    'random_word': random_word,  # don't need to pass count here because it's a request.session above
  }

  return render(request, 'random_app/index.html', context=context)



