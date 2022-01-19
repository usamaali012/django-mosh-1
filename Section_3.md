# SECTION 3

# First Process of every project is to figuring out the pieces of data we want to store. Depends on requirement on our application
# Relationships:
	- 1 to 1
	- 1 to Many
	- Many to Many
# Always Design Your Models Based on the requirements of your project.

# ASSOSIATION CLASS:
	 - Which represents the relationship between other 2 classes (tables) who are in Many to Many Relationship. e.g., Contacts and Groups are two classes which are in many to many relationship and we create an assosiation class called GroupContacts which shows relationship between these classes.
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