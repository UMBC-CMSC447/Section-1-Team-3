This is the base code for Django.

Contents

PART A: Installing Virtual Environment
PART B: Running Virtual Environment
PART C: Notes

##############################################################

PART A: Installing Virtual Environment

Note: Commands run from command line are prefeaced with $

NEW INSTRUCTIONS:

1. Install python 2.7

	Check if already installed:
	
	$ python --version

	Install:
	Windows:
		https://www.python.org/downloads/
	Linux
		#apt-get install python

2. Install pip if not already installed (very likily that it is)

	Update it just in case it is not up to date
		$ python -m pip install --upgrade pip

	If not already Installed
	Linux:
		# apt-get install python-pip

3a. Install python virtual enviroment:

	$ pip install virtualenv

3b. Set up virtual environment

	To create folder venv (or name of your choosing) containing python executables and copy of pip library to install other packages

	$ virtualenv venv

	Reference: http://docs.python-guide.org/en/latest/dev/virtualenvs/

	NOTES: It is a good idea to install this in an easy to get to place. You will will need to go to the directory and activate the virtual environment everytime you want to run the application.

	Suggest making the directory and then clone the git repo again inside of that directory.

	The virtual enviroment does not modify system files or configurations, it is just a standalone python install to a directory. Copy and paste completely moves it and deleteing the directory removes it.)

	The virtual enviroment installs python in a local directory. This way we can keep all of the extra packages (django, mangoDB, South) we need in a single directory. At the end we can zip the directory and upload it to our repo as a deployable product.

4. Activate your virtual enviroment

windows:
	$ Scripts\activate
linux:
	$ source venv/bin/activate

Packages

5. DJANGO.

	In order to get Django to work with mongo we need to install a special version of Django that works with no-rel database structures like mongo. To do this we need to install Django from source.

5a. Go to this git repo:
		https://github.com/django-nonrel/django

5b. Click on the "Download ZIP" button to download a zip of the repo
	
5c. Unzip the folder in your virtual enviroment

5d. From within your ACTIVATED virtual enviroment run the following commands:

		$ python setup.py build
		$ python setup.py install

6. Install MangoDB engine for django

	From ACTIVATED virtual environment:

6a. Install Djangotoolbox

	$pip install git+https://github.com/django-nonrel/djangotoolbox

6b. Install Django MongoDB Engine

	$pip install git+https://github.com/django-nonrel/mongodb-engine

	Reference: http://django-mongodb-engine.readthedocs.org/en/latest/topics/setup.html

	Note: DATABASE IS ALREADY CONFIGURED so no need to worry about that last step in the full instructions.

7. Install South

	$ pip install south

8. Check packages

	From ACTIVATED virtual environment

	$ pip freeze

	to list all installed packagesYou should see this:

	Django==1.6.11
	django-mongodb-engine==0.6.0
	djangotoolbox==1.8.0
	pymongo==3.2.2
	South==1.0.2

Install Complete

PART B: Running Virtual Environment

You should have completed Part A at this point.

To Run the Server:

1. Enter virtual environment:

	windows:
		$ Scripts\activate
	linux:
		$ source venv/bin/activate

2. Change directory:

	Section-1-Team-3/Code/mysite

3. Start Server

	$ python manage.py runserver


The server is now running, use CNTL-C to kill it

	Visit:

		http://127.0.0.1:8000/polls/
		http://127.0.0.1:8000/beach_homepage/index.html


PART C: Notes

	Runserver command starts the dev server on the internal IP at port 8000

	Now we have a deployable enviroment that we can put anywhere, as long as we do all the configuration in the pyhon virtual enviroment.

	If you add any packages, check which packages with $ pip freeze and please add them to the list in step 8.

	Important Files: (PLEASE ADD TO THIS LIST)

	mysite/mysite/settings.py
	mysite/mysite/urls.py
	mysite/beach_homepage/views.py
	mysite/login/*