from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):

  return render(request, 'surveyForm_app/index.html')


def result(request):
   
  try:
    request.session['count'] 
  except KeyError:
    request.session['count'] = 0
  request.session['count'] += 1


  if request.method == 'GET':
    return redirect('/')



def process(request):

  if request.method == 'POST':
    form = submissionForm(request.POST)
    if form.is_valid():

      context = {
        'name': request.form['name'],
        'location': request.form['location'],
        'language': request.form['language'],
        'comment': request.form['comment']
      }

    else:
      form = submissionForm()

  return render_template(request, 'surveyForm_app/result.html', context=context)
