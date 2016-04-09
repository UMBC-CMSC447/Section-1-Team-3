This is the base code for Django. On your individual development enviroments use the following commands to start the application:

Note commands run from command line are prefeaced with $ or are specified with quotes
NEW INSTRUCTIONS:
-First step is install python 3.5

-Install pip if not already installed (very likily that it is) 

-Next, install a python virtual enviroment:

NOTE: It is generally a good idea to install this in an easy to get to place as you will need 
to go to the directory and activate it everytime you want to run the application.
(I chose to make the directory and then clone the git repo again inside of that direcotry.This 
is of course up to you and can always be changed. The virtual enviroment does not
modify system files or configurations, it is just a standalone python install to a 
directory. Copy and paste completely moves it and deleteing the directory removes it.)

http://docs.python-guide.org/en/latest/dev/virtualenvs/#virtualenvironments-ref

The general idea of the virtual enviroment is that it installs python in a local directory.
This way we can keep all of the extra packages (like django) we need in a single directory,
this way at the end we can zip the directory and upload it to our repo and now we have a 
deployable product.

If you are curious as to why we are not uploading the virutal enviroment itself to the git repo,
I refer you to this:
http://stackoverflow.com/questions/6590688/is-it-bad-to-have-my-virtualenv-directory-inside-my-git-repository

-Now activate you virtual enviroment as shown before and install Django

Full Instructions:https://docs.djangoproject.com/en/1.9/topics/install/#installing-official-release

	The part you need:

	Activate the virtual enviroment by running Scripts\activate
	From you virtual enviroment run the following command:
	$ pip install Django

-Install Mango DB engine for django

You can use this for referance but DO NOT FOLLOW IT! FOLLOW THE INSTRUCTIONS HERE INSTEAD:
Since you already have a django virtual enviroment installed all you need to do is run these commands
from the virtual enviroment:

$pip install djangotoolbox
$pip install git+https://github.com/django-nonrel/djangotoolbox

now everything is installed and your if you run "pip freeze" to get a list of installed packages it should read:
Django==1.9.5
django-mongodb-engine==0.6.0
djangotoolbox==1.8.0
pymongo==3.2.2


-Still staying inside your virtual enviroment, change directories to mysite folder which contains the django code
-You can start the server with $ python manage.py runserver
-Now the server is running, use CNTL-C to kill it

To access the poll page go to this url: http://127.0.0.1:8000/polls/

Now we have a deployable enviroment that we can put anywhere,
as long as we do all the configuration in the pyhon virtual enviroment.
To see what packages you have installed use the "pip freeze" command
If you have any packages installed that do not already appear in our requirements.txt
add them to it. 