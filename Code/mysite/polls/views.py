from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.generic import ListView
from polls.models import property
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, View
# Create your views here.
import json
from django.http import HttpResponse

def MyView(request):
    properties = property.objects.all()
    context = RequestContext(request)
    
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "I am bold font from the context"}
    
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render_to_response('polls/index.html', {'list':properties},context)
 
    
def index(request):        #return HttpResponse("Hello, world. You're at the polls index.")
        # Request the context of the request.
        # The context contains information such as the client's machine details, for example.
    properties = property.objects.all()
    context = RequestContext(request)
        
        # Construct a dictionary to pass to the template engine as its context.
        # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "I am bold font from the context"}
        
        # Return a rendered response to send to the client.
        # We make use of the shortcut function to make our lives easier.
        # Note that the first parameter is the template we wish to use.
    return render_to_response('polls/index.html', {'list':properties},context)
        
        
class CreatePropertyView(CreateView):
    model = property
    template_name = 'edit_property.html'
    def get_success_rul(self):
        return reverse('contacts-list')

