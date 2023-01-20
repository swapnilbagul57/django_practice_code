from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def members(request):
    return HttpResponse("Hello Team, we are ready to create new prpject in django")


from django.template import loader

def display(request):
  template = loader.get_template('my_first.html')
  return HttpResponse(template.render())

def testing(request):
  template = loader.get_template('my_first.html')
  context = {
    'firstname': 'Swapnil',
  }
  return HttpResponse(template.render(context, request))


def tested(request):
  template = loader.get_template('my_first.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],
  }
  return HttpResponse(template.render(context, request))