# Admin Interface
	- Every Django app comes with an admin interface.   '/admin'
	- Create super user for admin through terminal.
	- python manage.py createsuperuser
	- session app (default django app) is used for temporarily storing user's data.
	- To change admin/superuser's password:
	- python manage.py changepassword admin
	- Admin interface has a built-in header 'Django administration'
	- To chnage it go to urls.py file of main project and write:
	- admin.site.site_header = 'Storefront Admin'
	- To change second heading in admin app:
	- admin.site.index_title = 'Admin'  


# Registering Models in Django Admin:
	- Registering models so that we can manage them in admin site
	- In each app, there is a file called admin.py.
	- Here we customize the admin panel for this app
	- And models are registered here.
	- You can change default representation of model object.
	- How to modify string representation of an object in Python. --> (Override __str__ method for that class)
	- Every python object has this method '__str__' which is called when that object is converted into string.
	- Default name for each object is 'className object(objectNumber)'
	- To change this default name to something else, override '__str__' method.
	
	- Sorting Objects of a class by their title.
	- define a 'Meta Class' inside that class.
	- class Meta:
          ordering = ['title']


# Customizing The List Page:
	- List Page is the pasge where all the objects of your class are showing.
	- Create a new class  by name 'NameofModelAdmin' ==> 'ProductAdmin' in admin.py file.
	- Class should inherit from 'admin.ModelAdmin'
	- With this class we can specify how we wanna view or edit the products on admin site
	- In this class we can set a bunch of attributes to customize the list page.
	- To modify list_display, we can say:
	- list_display = ['title', 'unit_price']
	- We also have to register this class with its model.
	- Or we can use the decorator for this too above the class definition:
	- @admin.register(models.Product)
	- With above decorator, we will NOT be needing following line to register our Model.
	- admin.site.register(models.Product, ProductAdmin)
	- If you want to be able to edit fields on list page give this attribute in the ProductAdmin class.
	- list_editable = ['unit_price'] --> In array specify any fields of your model.
	- To see limited number of objects on list page:
	- list_per_page = 10



# Adding Computed Column:
	- Depending on a field value, showing something else on the table.
	- list_display = ['title', 'unit_price', 'inventory_status']
	- @admin.display(ordering='inventory')
    - def inventory_status(self, product):
          if product.inventory < 10:
              return 'Low'
          return 'OK'
    - This will add a column in list with name inventory status, but instead of showing inventory it will show Low or OK based on the number of products we have. If the inventory is less than 10 it will show Low wlse it will show OK



# Selecting Related Objects:
	- list_display = ['title', 'unit_price', 'inventory_status', 'collection']
	- Here we are adding collection column which is a realted class of product. 
	- But it will show us the string representation of collection class which we have set to title of collection.	
	- If you want to show a particular field of related class. For this we have to define a method.
	- But first preload the related class so that we do NOT have to send individual query for each product.


# Overriding the Base QuerySet:
	- Sometimes we have to override the base QuerySet which is used to render the list page.
	- If we want to display a column which is neither in Model or any of its related models, we need to annotate and compute that column,
	- For this we need to override 'get_queryset' method of 'ModelAdmin class'

	- @admin.register(models.Collection)
	- class CollectionAdmin(admin.ModelAdmin):
    - list_display = ['title', 'products_count']                       --> Simple list display of two columns in Collection page

    - @admin.display(ordering='products_count')                        --> To make this column sortable.
    - def products_count(self, collection):                            --> products_count is not a field in Collection model
          return collection.products_count                             --> So definig a method for it.

    - def get_queryset(self, request):                                
          return super().get_queryset(request).annotate(         --> Annontate will add this field to this model on the runtime
              products_count=Count('product')                    --> overriding queryset method.
          )


# Providing Links to other pages:
	- Adding Foriegn Key Links to related columns.
	- We have to make this html link. Which will lead us to the list of realted model.
	- from django.utils.html import format_html
	- format_html('<a href="https://google.com">{}</a>', collection.products_count)
	- With this link, every row in products_count field becomes a link to google page.
	- But we want to send it to product page. For that we need to find link to product page.
	- To get url we'll use 'from django.urls import reverse'
	- reverse function takes a special arguument reverse(admin:app_model_page)
	- reverse('admin:store_product_changelist')
	- changelist is the name for the page where list of product is shown.
	- This will take us to the whole list of products.
	- But we only want to show the products which are in that current collection.
	- For that we have to add a query string to our url dynamically.
	- The query string looks like this:
	- url/?collection__id=3
	- To add a query string to our url we'll use 'from django.utils.html import urlencode'
	- url = (reverse('admin:store_product_changelist') + '?' + urlencode({'collection__id': collection.id}))


# Adding Search to the List Page:
	- To add searching fields in your list, use:
	- search_fields= ['first_name', 'last_name']
	- This will create a search bar where if we enter something, it will seach first and last name.
	- But if you type only 'b' in search bar this will bring every name that conatins b in it.
	- So we'll modify our search fields with a lookup field.
	- search_fields= ['first_name__startswith', 'last_name__startswith']
	- Now this search is also case-sensitive.
	- To make it insensitive:
	- search_fields= ['first_name__istartswith', 'last_name__istartswith']


# Adding Filter to the List Page:
	- list_filter = ['collection', 'last_update']
	- This will add a side bar of 2 filters. collection and last_update.
	- Now we can easily filter products on these basis.
	- This is a built-in filters.
	- Now custom filters:
	- create a new class which will inherit from 'admin.SimpleListFilter'
	- add title and parameter_name attributes. (name=name of filter), (parameter_name= parameter name to show up in querystring)
	- Now add two methods (lookups and queryset)
	- 'lookups' should return list of tuples. A tuple should contain 2 values. First is actual value used for filtering and 2nd value is human readable description for that value. [('<10', 'Low')]
	- 'queryset' is where we implement filtering logic.
	- In this function 'self.value()' returns selected filter. 
	- And here you can add your query to filter your products as you desire.
	- Write this class name to where you want to apply this filter in list_filter list.
	-  list_filter = ['collection', 'last_update', InventoryFilter]


# Creating Custom Actions:
	- Every List Page Comes with an Action drop down menu which contains Delete Selected Product Option.
	- We can extend this list and register our own custom actions.
	- Setting inventory of product to zero (Custom Action)
	- For the list we want a custom action, we need to add a function in Admin class of the model of that list.
	- And add a following decorator on top of that function.
	- Every model admin has a built-in function "message_user" for showing a message to user.
	- @admin.action(description="Clear inventory")
    - def clear_inventory(self, request, queryset):
    - 	updated_count = queryset.update(inventory=0)
    -   self.message_user(
            request,
            f'{updated_count} products were successfully updated.',
            messages.SUCCESS                                               --->> Message Type.
        )
	- Now to show this action to the user, add this action (function you have defined) to the Admin class of that list, like:
	- action = ['clear_inventory']


# Customizing Forms:
	- Django Admin has forms for every model to add items into it.
	- Every model has its own kind of form having its own fields. 
	- Go to the Admin classof that model which you want to modify.
	- fields = ['title']               --->> add only fields that are in this list from that model in its form.
	- exclude = ['title']              --->> Exclude fields from the form which are in this list.
	- readonly_fields = ['promotions'] --->> This will only appear as readonly field. You will NOT be able to dit it. 
	
	- Now::
	- Auto-populating the slug field in the Product Model form.
	- prepopulated_fields = {
        'slug': ['title']
    }
    - For this method to work, you should NOT touch the field which you want to populate.
    - Because if you do, this will stop working.

    - At the moment, we have a drop down menu for collection filed, in our product page.
    - This is showing all the collection in our database.
    - Dropdown can be hard to follow if number of collections become more than 100 or a certain value.
    - So changing this to a Auto-Complete field.
    - autocomplete_fields = ['collection']
    - But for this to work, we also have to add search_fields in the CollectionAdmin class because django does NOT know how to search for collection. 
    - search_fields = ['title']          --->> Searching with title field.
    - To find all the options go to The Django Admin site -->> ModelAdmin Options -->> Admin actions


# Adding Data Validation:
	- By Default our forms include basic data validation logic.
	- Like if we leave a field empty while creating a product it will give an error.
	- But it does the same for nullable fields also. -->> if we have set that field to null=True,
	- Because "null=True" only works for databases.
	- To make this not give an error for a field (while creating and leaving a field empty) set another field.
	- "blank=True"

	- But we do NOT have any validator for wrong values.
	- For that we have to bring validators in play. 
	- unit_price = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
        validators=[MinValueValidator(1)]
        )
    - Now this will not let any negative or zero value as price of product. 



# Editing Children Using Inlines:
	-  If a class/model is dependent on another class, we can define the Admin model class for the child model and that class can inehrit either from "admin.TabularInline" or "admin.StackedInLine"
	- class OrderItemInLine(admin.TabularInline):
      	model = models.OrderItem
	- And in parent class add a field:
	- inlines = [OrderItemInLine] 
	- 'OrderItemInLine' class that we have created indirectly inherits from 'admin.ModelAdmin' class.
	- So all the functionality that we have seen can also apply here.
	- 3 rows for inline child class is default.
	- if you want to change it, you can set field:
	- extra = 0
	- To limit the no. of order item rows in form page, we can:
	- min_num = 1
	- max_num = 10

	- "TabularInline" shows a table form in which each row is a new entry in child table and the columns are fields of child table.
	- "StackedInLine" does NOT have columns. In this fileds of each entry of child class shows up as rows stacked on each other.