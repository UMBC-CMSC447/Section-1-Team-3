from django.shortcuts import render
from regProperty.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

@csrf_protect
def propregister(request):
    if request.method == 'POST':
        form = PropRegistrationForm(request.POST)
        if form.is_valid():
            prop = property.objects.create(
                Name=form.cleaned_data['Name'],
                Price=form.cleaned_data['Price'],
                Location=form.cleaned_data['Location'],
                Owner=form.cleaned_data['Owner']
            )
            return HttpResponseRedirect('/propregister/success/')
    else:
        form = PropRegistrationForm()
        
    variables = RequestContext(request, {
        'form': form
    })
    return render_to_response(
    'propregistration/register.html',
    variables,
    )
 
def propregister_success(request):
    return render_to_response(
    'propregistration/success.html',
    )
 
#def logout_page(request):
#    logout(request)
#    return HttpResponseRedirect('/')
 
#@login_required
#def home(request):
#    return render_to_response(
#    'home.html',
#    { 'user': request.user }
#    )
