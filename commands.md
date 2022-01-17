# SECTION 2

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





# SECTION 3

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





# SECTION 4:
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

# Populating database with Dummy Data:
	- use website mockaroo.com





# SECTION 5:

# Every Model in Django has an attribute called 'objects'. This returns a manager object.
	- A manager is an interface to the database
	- Its like a remote control with the bunch of buttons that we can use to talk to our database.
	- In this object (manager object) we have methods for querying and updating our database. e.g., 
	- .all() --> for pulling out all the objects in our table/Model.
	- .get() --> for getting a single object
	- .filter() --> For filtering data, etc.
	- Most of these methods returns a QuerySet object. e.g., all above methods.
	- On the contrary, we have some methods that returns result right away. e.g., 
	- .count() --> returns thr number of no. of records in the model/table.
	- QuerySet is an object  that encapsulate a query.
	- Django Evaluates this QuerySet, and then it will generate the right SQL statement to send to our database.
	- It does NOT always generate/evaluate a SQL statement but only for few scenarios. e.g., using .all() and loopinh through all objects.
	- One scenario where QuerySet is evaluated is when we iterate over it.
	- Another scenario is when we convert it to a list. 
	- 3rd scenario is when we access an individual element or elements.
	- Because it does NOT always evaluate right away we say, QuerySet is lazy meaning that they are evaluated at a later point.
	- We can use QuerySet methods (.all(), .filter(). order_by() etc.) to build complex queries. We can also chain all these methods to build a complex query.

# Always pay great attention to the name of your variables and functions.

# Methods for retrieving objects:
	- .all() --> returns a QuerySet. e.g.,
	- query_set = Product.objects.all() --> When this is evaluated, we get all the objects in given table (Product table)
	- .get() --> To get a single object. e.g.,
	- product = Product.objects.get(id=1) |or| product = Product.objects.get(pk=1)
	- pk stands for Primary Key. When we use 'pk' djnago will automatically translate this to the name of the primary key field. 
	- .get() methods returns an object not a QuerySet. Because with a single object we can NOT do any other queries or apply any filters.
	- .filter() returns a QuerySet.


# Some Code Lines for QuerySets and Managers:
	- query_set = Product.objects.all()
    - for product in query_set:
    -     print(product)

    - product = Product.objects.get(id=1)

    - product = Product.objects.get(pk=1)

    - products = list(query_set)

    - product_1 = query_set[0]

    - product_1_5 = query_set[0:5]

    - try:
    -     product = Product.objects.get(pk=0)
    - except ObjectDoesNotExist:
          ...

    - product = Product.objects.filter(pk=0).first()   --> Returns object. If the object does NOT exist it returns None.

    - exists = Product.objects.filter(pk=0).exists()  --> Returns True or False.



# Filtering Objects:
	- product = Product.objects.filter()
	- For filter we pass keyword argument. For exapmle, for looking up products that are worth $20, we write:
	- product = Product.objects.filter(unit_price=20)

	- We cannot pass logical operators in filter like > < etc.
	- To make a logical filter, we use QyerySet Type or lookup type like (filter_object_name__gt=20)
	- __gt = greater-than
	- __gte = greater-than-or-equal-to
	- __lt = less-than
	- __lte = less-than-or-equal-to
	- __range = (20, 30)
	- Example:
	- product = Product.objects.filter(unit_price__gt=20)
	- product = Product.objects.filter(unit_price__range=(2, 30))

# Filtering through relationships: (Examples)
	- filter(NameOfRelatedClass__AttributeName=AttributeValue)
	- query_set = Product.objects.filter(collection__id=1)
	- query_set = Product.objects.filter(collection__id__gt=1)
	- query_set = Product.objects.filter(collection__id__range=(1, 2, 3))

# Filtering Options for Strings: (Example)
	- use __contains for case-sensitive and use __icontains for case-insensitive
	- filter(AttributeName__contains='AttributeValue')
	- query_set = Product.objects.filter(title__icontains='coffee')
	- query_set = Product.objects.filter(title__contains='coffee')
	- __startswith, __endswithcetc.
	- To see if an object has an attribute with null value
	- query_set = Product.objects.filter(description__isnull=True)

# Date Filtering:
	- use __year=value
	filter(AttributeName__year=YearValue)
	- query_set = Product.objects.filter(last_update__year=2021)
