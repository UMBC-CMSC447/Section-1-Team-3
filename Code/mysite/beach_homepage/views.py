from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import render
from beach_homepage.models import property
from polls.models import UserAvatar
from beach_homepage.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.http import HttpResponse
from datetime import datetime as dt
import re
import json
# Create your views here.

dict = {'Ocean City' : [38.336502, -75.084908], 'Park Place' : [36.863140,-76.015778]}


def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    print("RANDOM IDEX")
    jsonDec = json.decoder.JSONDecoder()
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
    properties = property.objects.all()
    test = []
    print("I AM SENDING YOU TO ", newPath)
    username = request.user
    print(request.user)


    for house in properties:
        text = house.RentSlots
        myPythonList = []
        if(text):
            myPythonList = jsonDec.decode(house.RentSlots)
            print("+++++FOUND A THING+++++")
        house.RentSlots = myPythonList
        print("TENT SLOT")
        print(house.RentSlots)
        #print("Looking at " + house.Owner + " and " + str(username))
        if house.Owner == str(username):
            test.append(house)
            #print("FOUND A HOUSE")

    if(newPath == "beach_homepage/user_profile.html"):
        print("!!!!GOING TO USER PROFILE!!!!")
        image = ""
        useObj = UserAvatar.objects.all()
        for obj in useObj:
            print("Looking at")
            if str(obj.username) == str(username):
                print("FOUND THE PROPER AVATAR")
                image = obj.avatar
        return render_to_response(newPath,{'list':properties, 'avatar':image},context)
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    #return render_to_response(newPath, {'user' : request.user,'house' : test}, context)
    return render_to_response(newPath,{'list':properties},context)

def beach_index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")

    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)
    #to parse request object
    #https://code.djangoproject.com/wiki/HttpRsequest
    newPath = "beach_homepage/index.html"
    print("-----------INDEX----------")
    print(request.path)
    print("beach_homepage/index.html")
    print(newPath)
    print("---------------------")

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "I am bold font from the context"}
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    #return render_to_response(newPath, {'user' : request.user,'house' : test}, context)
    #return HttpResponseRedirect("beach_homepage/index.html")
    #return render_to_response("beach_homepage/index.html",context)
    return HttpResponseRedirect("/beach_homepage/index.html")

def beach_redirect(request):
    print("redirect!!")
    context = RequestContext(request)
    #to parse request object
    #https://code.djangoproject.com/wiki/HttpRsequest
    newPath = request.path[1:]
    newPath = re.split('/',newPath)
    print("-----------INDEX----------")
    print(request.path)
    print("beach_homepage/index.html")
    print(newPath)
    newPath = "/" + newPath[0] + "/" + newPath[2]
    print("now")
    print(newPath)
    print("---------------------")
    return HttpResponseRedirect(newPath)

def beach_user_info(request, data):
    print("&&&USERINGOFOFOFO")
    print(data)
    print(request.path)
    print("AFter new things")
    useObj = UserAvatar.objects.all()
    context = RequestContext(request)
    #to parse request object
    #https://code.djangoproject.com/wiki/HttpRsequest
    newPath = request.path[1:]
    newPath = re.split('/',newPath)
    username = str(newPath[2])
    print("-----------FINDING ALL TEH USERS----------")
    print(request.path)
    print("beach_homepage/index.html")
    print(newPath)
    newPath = "/" + newPath[0] + "/" + newPath[2]
    newPath = "beach_homepage/user_info.html"
    print("now")
    print(newPath)
    print("---------------------")
    foundUsername = ""
    foundAvatar = ""
    foundUsername = username
    for obj in useObj:
        print("Looking at")
        if str(obj.username) == str(username):
            print("FOUND THE PROPER AVATAR")
            foundAvatar = obj.avatar
    return render_to_response(newPath,{'username':foundUsername, 'Image':foundAvatar},context)


def beach_prop_info(request, data):
    jsonDec = json.decoder.JSONDecoder()
    context = RequestContext(request)
    properties = property.objects.all()
    foundProp = property.objects.all()
    newPath = request.path[1:]
    newPath = re.split('/',newPath)
    username = str(request.user)
    canRate = False
    #print("The new path is:" + newPath[2])
    for house in property.objects.all():
        #print("Looking at " + house.Name + " and " + newPath[2])
        if house.Name == newPath[2]:
            foundProp = house
            text = foundProp.RentSlots
            myPythonList = []
            if(text):
                myPythonList = jsonDec.decode(foundProp.RentSlots)
            listToSend = []
            for slot in myPythonList:
                slot = re.split(',',slot)
                listToSend.append(slot)
                print(slot)
            #print("*****LIST OF RENTS TO SEND********")
            print(listToSend)
            foundProp.RentSlots = listToSend
            #print("TEST098098")
            print(foundProp.RentSlots)
            #if house.Location in dict:
            #    place_lat = dict[house.Location][0]
            #    place_long = dict[house.Location][1]
            #print("FOUND")

    print("&&looking at slots&&")
    for slot in foundProp.RentSlots:
        if(str(slot[0]) == str(username)):
                canRate = True

    print("-----------INDEX----------")
    print(request.path)
    print("beach_homepage/index.html")
    print(newPath)
    newPath = "beach_homepage/prop_info.html"
    print("---------------------")
    print("CONTECXT")
    print(context)
    message = ""
    return render_to_response(newPath,{'list':foundProp, 'message':message, 'canRate':canRate},context)



def sort(request,data):
    return HttpResponseRedirect("/beach_homepage/index.html")
@csrf_protect
def beach_rentProperty(request, data):
    jsonDec = json.decoder.JSONDecoder()
    context = RequestContext(request)
    properties = property.objects.all()
    foundProp = property.objects.all()
    newPath = request.path[1:]
    newPath = re.split('/',newPath)
    form = request.POST
    myUser = form["user"]
    myStart = form["start"]
    myEnd = form["end"]
    rentInfo =  str(myUser) + "," + str(myStart) + "," + str(myEnd)
    myStart  = re.split('-',myStart)
    myStart = dt(int(myStart[0]),int(myStart[1]),int(myStart[2]))
    myEnd  = re.split('-',myEnd)
    myEnd = dt(int(myEnd[0]),int(myEnd[1]),int(myEnd[2]))

    print("INFO!!!")
    print(myUser, " ", myStart, " ", myEnd)
    print(rentInfo)
    print("endINFO")
    print(form)
    print("Data")
    print(data)

    rentValid = True
    #determine if rent is valid
    for house in property.objects.all():
        print("Looking at " + house.Name + " and " + newPath[2])
        if house.Name == newPath[2]:
            foundProp = house
            foundProp.Rent = 0
            myPythonList = []
            myPythonList.append(rentInfo)
            text = foundProp.RentSlots
            #check if any previous rents
            if(text):
                myPythonList = jsonDec.decode(foundProp.RentSlots)
                print(myPythonList[0])
                print("********WHAT I NEED**********")
                for slot in myPythonList:
                    slot = re.split(',',slot)
                    #start is slot[1]
                    tryStart  = re.split('-',str(slot[1]))
                    tryStart = dt(int(tryStart[0]),int(tryStart[1]),int(tryStart[2]))
                    #end is slot[2]
                    tryEnd  = re.split('-',str(slot[2]))
                    tryEnd = dt(int(tryEnd[0]),int(tryEnd[1]),int(tryEnd[2]))
                    #if x is inbwtween y
                    if(myStart >= tryStart and myStart <= tryEnd):
                        rentValid = False
                    if(myEnd >= tryStart and myEnd <= tryEnd):
                        rentValud = False
                    if(tryStart >= myStart and tryStart <= myEnd):
                        rentValid = False
                    if(tryEnd >= myStart and tryEnd <= myEnd):
                        rentValud = False

    #print("The new path is:" + newPath)
    if(rentValid == True):
        for house in property.objects.all():
            #print("Looking at " + house.Name + " and " + newPath[2])
            if house.Name == newPath[2]:
                foundProp = house
                foundProp.Rent = 0
                myPythonList = []
                myPythonList.append(rentInfo)
                text = foundProp.RentSlots
                #print("THE TEXT OF TExT @$#$#")
                print(text)
                if(text):
                    #print("NOT*EMPTY^^^^")
                    myPythonList = jsonDec.decode(foundProp.RentSlots)
                    myPythonList.append(rentInfo)
                else:
                    print("EMPYT******")
                #print("FULL LIST!!!!!")
                print(myPythonList)
                #print("end of list------------------")
                foundProp.RentSlots = json.dumps(myPythonList)
                foundProp.save()
                #print("FOUND")
    print("-----------RENTING----------")
    print(request.path)
    #print("beach_homepage/index.html")
    #print(newPath)
    newPath = "/beach_homepage/prop_info/" + newPath[2]
    #print("NOW NEW PATH IS!!! = " + newPath)
    #print("---------------------")
    #beach_redirect(newPath)
    #return render_to_response("/beach_homepage/prop_info/property_search.html",{'list':foundProp},context)
    #return HttpResponseRedirect("/beach_homepage/property_search.html")
    return HttpResponseRedirect(newPath)

def beach_ApproveProperty(request, data):
    context = RequestContext(request)
    properties = property.objects.all()
    foundProp = property.objects.all()
    newPath = request.path[1:]
    newPath = re.split('/',newPath)
    form = request.POST
    print(form)
    print("Data")
    print(data)
    #print("The new path is:" + newPath)
    for house in property.objects.all():
        print("Looking at " + house.Name + " and " + newPath[2])
        if house.Name == newPath[2]:
            foundProp = house
            foundProp.Approval = 1
            foundProp.save()
            print("FOUND")
    print("-----------APRROVING----------")
    print(request.path)
    print("beach_homepage/index.html")
    print(newPath)
    newPath = "/beach_homepage/prop_info/" + newPath[2]
    print("NOW NEW PATH IS!!! = " + newPath)
    print("---------------------")
    #beach_redirect(newPath)
    #return render_to_response("/beach_homepage/prop_info/property_search.html",{'list':foundProp},context)
    #return HttpResponseRedirect("/beach_homepage/property_search.html")
    return HttpResponseRedirect(newPath)

def beach_RateProperty(request, data):
    context = RequestContext(request)
    properties = property.objects.all()
    foundProp = property.objects.all()
    newPath = request.path[1:]
    newPath = re.split('/',newPath)
    form = request.POST
    myRating = form["rating"]
    print(form)
    print("Data")
    print(data)
    print("!!RATING = ", myRating)
    print(myRating)
    print("!!RATINGPATH!!!")
    print(newPath)
    #print("The new path is:" + newPath)
    for house in property.objects.all():
        #print("Looking at " + house.Name + " and " + newPath[2])
        if house.Name == newPath[2]:
            foundProp = house
            if(foundProp.Rating == 0):
                foundProp.Rating = int(myRating)
            foundProp.Rating = (foundProp.Rating + int(myRating)) /2
            foundProp.save()
            print("FOUND")
    print("-----------RENTING----------")
    print(request.path)
    print("beach_homepage/index.html")
    print(newPath)
    newPath = "/beach_homepage/prop_info/" + newPath[2]
    print("NOW NEW PATH IS!!! = " + newPath)
    print("---------------------")
    #beach_redirect(newPath)
    #return render_to_response("/beach_homepage/prop_info/property_search.html",{'list':foundProp},context)
    #return HttpResponseRedirect("/beach_homepage/property_search.html")
    return HttpResponseRedirect(newPath)


def beach_unApproveProperty(request, data):
    context = RequestContext(request)
    properties = property.objects.all()
    foundProp = property.objects.all()
    newPath = request.path[1:]
    newPath = re.split('/',newPath)
    form = request.POST
    print(form)
    print("Data")
    print(data)
    #print("The new path is:" + newPath)
    for house in property.objects.all():
        print("Looking at " + house.Name + " and " + newPath[2])
        if house.Name == newPath[2]:
            foundProp = house
            foundProp.Approval = 0
            foundProp.save()
            print("FOUND")
    print("-----------RENTING----------")
    print(request.path)
    print("beach_homepage/index.html")
    print(newPath)
    newPath = "/beach_homepage/prop_info/" + newPath[2]
    print("NOW NEW PATH IS!!! = " + newPath)
    print("---------------------")
    #beach_redirect(newPath)
    #return render_to_response("/beach_homepage/prop_info/property_search.html",{'list':foundProp},context)
    #return HttpResponseRedirect("/beach_homepage/property_search.html")
    #return HttpResponseRedirect('/')
    return HttpResponseRedirect(newPath)

#full tutorial
#http://www.djangobook.com/en/2.0/chapter07.html
def search(request,data):
    context = RequestContext(request)
    properties = property.objects.all()
    foundProp = property.objects.all()
    newPath = request.path[1:]
    newPath = request.GET['currency']
    print("The new path is:" + request.GET['currency'])
    for house in property.objects.all():
        print("Looking at " + house.Name + " and " + newPath)
        if house.Name == newPath:
            foundProp = house
            print("FOUND")
    print("---------NEWONE------------")
    print(request.path)
    print("beach_homepage/index.html")
    print(newPath)
    print("---------------------")
    if request.GET['currency'] == "":
        return HttpResponseRedirect("/beach_homepage/property_search.html")
    if 'currency' in request.GET:
        sendPath = "prop_info/" + newPath
        message = 'You searched for: %r' % request.GET['currency']
        return HttpResponseRedirect(sendPath)
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)
@csrf_protect
def beach_propregister(request):
    print("I AM CALLED")
    if request.method == 'POST':
        print("GOT STEP ONE")
        form = PropRegistrationForm(request.POST,request.FILES)
        print(form)
        if form.is_valid():
            prop = property.objects.create(
                Name=form.cleaned_data['Name'],
                Price=form.cleaned_data['Price'],
                Location=form.cleaned_data['Location'],
                Lat=form.cleaned_data['Lat'],
                Long=form.cleaned_data['Long'],
                Image=form.cleaned_data['Image'],
                Owner=form.cleaned_data['Owner'],
                Description = form.cleaned_data['Description']
            )
            print("FORM WAS VALID AND REGISTERED")
            newPath = "/beach_homepage/prop_info/" + form.cleaned_data['Name']
            return HttpResponseRedirect(newPath)
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
@csrf_protect
def beach_userregister(request):
        print("I AM CALLED!!!")
        if request.method == 'POST':
            form = RegistrationForm(request.POST,request.FILES)
            if form.is_valid():
                user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email']
                )
                useravatar = UserAvatar.objects.create(
                username = form.cleaned_data['username'],
                avatar = form.cleaned_data['avatar']
                )
                print("AVATARTHINGS!!!!!")
                print(form.cleaned_data['avatar'])
                print(request.FILES)
                print("POST")
                print(request.POST)
                print(form.cleaned_data['username'])
                print("FORM WAS VALID AND REGISTERED")
                return HttpResponseRedirect('user_profile.html')
        else:
            form = RegistrationForm()

        variables = RequestContext(request, {
            'form': form
        })
        return render_to_response(
        'beach_homepage/create_user.html',
        variables,
        )
def userregister_success(request):
        print("SUCESS")
        return render_to_response(
        '/beach_homepage/user_profile.html',
        )
