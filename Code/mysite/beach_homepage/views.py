from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import render
from beach_homepage.models import property
from beach_homepage.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.http import HttpResponse
# Create your views here.


def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")

    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)
    #to parse request object
    #https://code.djangoproject.com/wiki/HttpRsequest
    newPath = request.path[1:]
    print("-----------INDEX----------")
    print(request.path)
    print("beach_homepage/index.html")
    print(newPath)
    print("---------------------")

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "I am bold font from the context"}
    test = property.objects.all()
    properties = property.objects.all()
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    #return render_to_response(newPath, {'user' : request.user,'house' : test}, context)
    return render_to_response(newPath,{'list':properties},context)

#full tutorial
#http://www.djangobook.com/en/2.0/chapter07.html
def search(request,data):
    #need to hardcode path to be beach_homepage/search
    newPath = request.path[1:]
    print("---------NEWONE------------")
    print(request.path)
    print("beach_homepage/index.html")
    print(newPath)
    print("---------------------")
    if 'q' in request.GET:
        message = 'You searched for: %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)
@csrf_protect
def beach_propregister(request):
    print("I AM CALLED")
    if request.method == 'POST':
        form = PropRegistrationForm(request.POST)
        if form.is_valid():
            prop = property.objects.create(
                Name=form.cleaned_data['Name'],
                Price=form.cleaned_data['Price'],
                Location=form.cleaned_data['Location'],
                Owner=form.cleaned_data['Owner']
            )
            print("FORM WAS VALID AND REGISTERED")
            return HttpResponseRedirect('property_search.html')
    else:
        form = PropRegistrationForm()

    variables = RequestContext(request, {
        'form': form
    })
    return render_to_response(
    'beach_homepage/list_new_property.html',
    variables,
    )

def propregister_success(request):
    return render_to_response(
    '/beach_homepage/property_search.html',
    )
