# SECTION 1

# installing django inside venv
--pipenv install django


# To go into venv
--pipenv shell


# To start project
django-admin startproject <projectname>


# manage.py file is a wrapper around django-admin



# To start server
--python manage.py runserver [portnumber(Optional)]



# TO see the venv directory
--pipenv --venv


# migrations folder in each app for generating database tables.
# admon.py to decide how admin page of our django app will look like
# app.py is place where we configure our app
# models.py is to design model classes for our app and to pull out data from our database
# views.py in NOT used for creating views. It is a RequestHandler for our app. Here we create view functions
# A view function takes a request and returns a response.  REQUEST -> RESPONSE
# urls.py is a file where we map our URLs to our view functions.
# views in django are called templates
# launch.json file is for vscode to know how to debug the appliction
# Middleware in settings.py is used to hook into django's request response processing





# SECTION 2

# First Process of every project is to figuring out the pieces of data we want to store. Depends on requirement on our application
# Relationships:
	- 1 to 1
	- 1 to Many
	- Many to Many
# Always Design Your Models Based on the requirements of your project.

# ASSOSIATION CLASS:
	 - Which represents the relationship between other 2 classes (tbales) who are in Many to Many Relationship. e.g., Contacts and Groups are two classes which are in many to many relationship and we create an assosiation class called GroupContacts which shows relationship between these classes.
- One Many-to-Many Relationship with an Assosiation Class or Two 1-to-Many Relationship

# Monolith:
	- When code becomes too big
# A good design is with MINIMAL COUPLING between Apps (Django) meaning and Apps does NOT depend on each other for their functionality.	
# HIGH COHESION (FOCUS) meaning each app is focused on a specific piece of functionality and includes everything needed to fulfil that piece of functionality.

# For Monetary Values, Always use DecimalField. FloatField have rounding issues.
# Django creates Primary_Key for each model class itself unless you create a field inside a class with attribure primary_key=True.


# Foriegn Key Constraints:
	- CASCADE: if the row in the parent table gets deleted the row in child table will also get deleted.
	- PROTECT: This will prevent deleting an entry in parent table if it has something assosiated in child table.
	- SET_NULL: if the row in the parent table gets deleted the row in child table will get set to null.
	- SET_DEFAULT: if the row in the parent table gets deleted the row in child table will get set to default.


# Many-to-Many Example:
- Promotion - Product
- Using ManyToManyField in one class, Django creates a reverse column in the other class. named as:
 "firstClassName_set"
 - Or you can supply a name to related_name an argument while defining ManyToManyField in one class.
 - If you want to avoid creating a reverse relationship in the other class set related_name to +. i,e., 
 - related_name='+'


# CIRCULAR DEPENDENCY:
	- CIRCULAR DEPENDENCY happens when two classes depend on each other at the same time. We should avoid it.

# 'django.contrib.contenttypes' (ContentType):
	 - using contenttypes, we can create generic relationships between our models. (it allows to have generic relationships)
	 - ContentType is a model that represents a type of an object in our application. 





# SECTION 3:
# Migrations:
	- In Django, we use migrations to create or update our database tables based off of the model we have in our project.

# python manage.py sqlmigrate [App_name] [migration_number (e.g., 0001, 0002)]:
	- using this command we can see the actual sql code that is sent to our database at runtime. 
	- the sql code will depend on (/be according to) the type of database backend we are using as our database.

# SEQUEL OR SQL
	- Originally SEQUEL (Structured English Query Language)
	- But SEQUEL was a trademark of an aircraft company.
	- That is why it was changed to SQL.
	- Called as both SQL and Sequel.

# METADATA:
	- class Meta: (Name of the class is important)
	- Used fr setting up extra details about the model. e,g., about database
	- Indexes in database are used to speed up our queries. 

# Undo Migrations:
	- To completely undo last migration:
	- Django assigns number to every migration e.g., 0001, 0002. To go back to previous migration use command:
	- python manage.py migrate [App_name] [migration_number] 
	- Plus you will have to delete the igration file as well as chnages in the code. (Use Git for that)

# Create an empty migration and there you can write arbitrary SQL code. TO have more control on your database.
	- python manage.py makemigrations [App_name] --empty
	- In RunSQL we can Provide two SQL statements separated by comma:
	- Use """ """ to write your SQL code in more than one line. 
	- 1: Upgrading our database, or
	- 2: Downgrading our database

