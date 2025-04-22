# 💻 Project Setup Guide

## XCode

Before getting started ensure that XCode is installed. https://developer.apple.com/xcode/ 

You can install via Terminal as well:

xcode-select --install

---

## Setting Up the CloudQuote GitHub Repository:
The following assumes that a GitHub username is already in place. To sign up for a GitHub account, visit the GitHub’s sign up page: https://github.com/signup 

Start by creating the repository in GitHub. 
Select the Repositories tab, then select New:

Next, select the Owner account and then provide a Repository name
Providing Description is optional but is a good habit to distinguish between multiple repositories

Choose whether the repository should be Public or Private. 
I've set the repository to Private while building the application. Once it's in a stable state, I will switch it to Public.
Add a README file ; another good habit and standard practice.
Choose a .gitignore template that aligns with your choice of language (e.g. Python)

Next choose a license. Some licenses are more permissible than others (e.g. MIT License, Apache 2.0, GNU General Public License 3.0) while others are less more permissible (e.g. GNU Lesser General Public License v2.1) . None (no license)  is also an option. 
Select Create repository to save your changes and create the repository

You will then be deposited into your new repository

---

## Generating an SSH Key

Previously, you could use the HTTPS:// protocol to set up git clone, but GitHub discontinued this option in 2021, likely for security reasons. Now, you must set up an SSH key on your local machine and add it to your GitHub account.

To set up an SSH key, open Terminal or the equivalent and type the following command ssh-keygen -t rsa -b 4096 -C "your_email@example.com"

For the location in which to save the file, I’m going to take the default location of /Users/heather/.ssh/id_rsa and hit enter.
You can choose to enter a passphrase for extra security. You will be prompted for a password and asked to reconfirm. 

Your key will then be saved in the default location of /Users/heather/.ssh/id_rsa

The private key is id_rsa . 
This key should never be shared and should always be kept secure.
The public key is id_rsa.pub.
This is the key that goes into GitHub.

---

## Adding the SSH Key to GitHub

Start by navigating to the directory where the public key is saved /Users/heather/.ssh/id_rsa and concatenate the contents by typing the following command:

cat /Users/heather/.ssh/id_rsa.pub

Copy the entire contents of the output of the command starting with ssh-rsa all the way through to the email address

Log into GitHub and click on your profile picture, then select Settings 

Then select SSH and GPG Keys from the left hand menu

Select New SSH key under the SSH key section

Provide a title for the key, keep the default selection for Key type as Authentication Key, paste the public key you copied above, and then select Add SSH key

Verify your identity (if applicable) 

Your SSH key is now linked to GitHub!

---

## Cloning Your Repository to Your Computer

Now that we’ve generated our SSH keys we should be able to clone the repository down to the desktop (or any other location preference)

cd /Users/heather/Desktop

To clone the repository, open Terminal and enter the following command:

git clone git@github.com:username/repository-name.git

Example:
git clone git@github.com:daheats/WhizQuote.git

Enter passphrase if prompted:

The repository is now cloned to Desktop with our starting contents
LICENSE
README.md

The GitHub repository is now linked to our local folder! 

---

## Setting Up a Virtual Environment & Packages

Developers use virtual environments to isolate project dependencies and to prevent conflicts between different projects while ensuring consistent setups across different systems.

To setup a new virtual environment with Python 3.11 for the project, open Terminal and run the following command:

python3 -m venv whiz-project-env


Next, we have to activate the virtual environment by running the following command:

source venv/bin/activate

---

## Setting Up the Backend (Django & Django Rest Framework)

Next, we’re going to install both Django and the Django Rest Framework into our virtual environment which will serve our backend:

pip install django
pip install django djangorestframework

---

## Setting Up the Frontend (Node.js & React)

Unlike Django and Django Rest Framework, Node doesn’t need a virtual environment to run in. 
Navigate to the following URL https://nodejs.org/ and download the Long Term Support version of Node.js.
In order to interact with Node and React, open a separate terminal keeping your other terminal with the Python virtual environment open. 
In order to start with React, we need to create a react project using the following command:

npx create-react-app whiz-frontend

Select y to proceed with the install

Run the following to start the server locally 

npm start


To test local setup, navigate to http://localhost:3000/ 

---

## Setting Up Your Database

To start, when developing locally, use the SQLite installation that comes with Python3. To confirm SQLite is installed run the following command:

python -c "import sqlite3; print(sqlite3.sqlite_version)"

The output should be something like the following:

3.37.0

---

## Setting Up Django

Within your virtual environment run the following command to start creating your django project:

django-admin startproject whiz_backend

Next, we’ll create a Django app for the API by running the following command:

python manage.py startapp api

Within the api folder the following directories exist:
__init__.py
Marks directory as a Python directory.
Importance: Without this, Python wouldn’t recognize api as a module and it wouldn’t be able to be imported.
Often empty and that’s fine.

apps.py
Contains application specific configurations and helps Django register apps properly.
Set the name of the application.
Define application specific settings or behaviors.
Register signals or perform initialization when the app is loaded.

admin.py
Register models with Django’s built in admin interface so they can be managed through the graphical user interface
Hooks your models into the Django Admin dashboard.


migrations
Tracks changes made to models and syncs changes with the database schema. 
Version control for your database.
	
models.py
Define data structures. 
File where you define Django models, which are Python classes that represent database tables. Each attribute in the class is a database field.
Common field types like CharField, TextField, IntegerField

tests.py
Where you write unit tests and integration tests.
Can test models, views, forms, APIs, and permissions.


views.py
Decide what to do when a user makes a request.
HTML pages, JSON, or redirects.


urls.py
Define url routes
Acts like a traffic controller


templates.py
Holds HTML files which Django uses to render views
Make sure DIRS is set in templates.py

---

## CORS

Cross-origin research sharing
Security feature built into web browsers

models.py

Every models.py file should start with: 

from django.db import models

This imports Django’s model module, which allows you to describe database tables in Python using classes. It includes fields like CharField, support for third-party extensions like django-money (for currency), and more. Basically, it’s like saying: “Hey Django, give me the stuff I need to define database tables in Python.”

Next, install django-money in the whiz-project-env virtual environment using pip. While we’re currently handling only USD, using django-money is considered best practice for handling currency in a structured and scalable way.

pip install django-money

Next, we’re going to import django-money into our models.py file so we can store and retrieve currency values. For example, amount: $49.99, currency: USD. This is like saying: “Hey Python, go grab me the special tool from django-money that helps me store money properly in the database.”

from djmoney.models.fields import MoneyField



