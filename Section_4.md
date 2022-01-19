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