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


# Complex Lookups:
	- Multiple Filters:
	- Condition is: inventory < 10 and price < 20. Multiple ways of Applying filter:
	- 1: Passing Multiple Keyword Arguments: 
	- query_set = Product.objects.filter(inventory__lt=10, unit_price__lt=20)
	- 2: Multiple filters: (.filter() method returns QuerySet, So we can filter to a filter)
	- query_set = Product.objects.filter(inventory__lt=10).filter(unit_price__lt=20)


# Q Objects: (Short for Query)
	- Using Q class, we can represent Query Expression and it produces a value.
	- Each Q object encapsulates a Query Expression or a Keywprd Argument. Example:
	- condition is: inventory < 10 OR price < 20.
	- query_set = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20))
	- query_set = Product.objects.filter(Q(inventory__lt=10) & ~Q(unit_price__lt=20))
	- Here | stands for OR. and & stands for AND and ~ stands for NOT.


# Referencing Fields:
	- Find all the products where their inventory = unit_price. (Comparing Two Fileds)
	- We CANNOT use following QuerySet for this:
	- query_set = Product.objects.filter(inventory=unit_price)
	- in Django, for such queries we use F Objects.


# F Objects:
	- using this class we can reference a particular field from the same table.
	- query_set = Product.objects.filter(inventory=F('unit_price'))
	- Using F Object, we can also reference fielf in a related table.
	- query_set = Product.objects.filter(inventory=F('collection__id')), In general:
	- F('relatedTableName__relatedTableFiled')


# Sorting Data:
	- .order_by() method helps us get data in a sorted way. We can sort data in one or more fields.
	- query_set = Product.objects.order_by('title')
	- In above queryset we have arranged data using title field in ascending order. For Descing order use '-' sign with filed name
	- query_set = Product.objects.order_by('-title')	
	- Sorting using multiple fileds.
	- query_set = Product.objects.order_by('unit_price', '-title')
	- With above query, we are sorting our data from cheapest to expensive, and if we have multiple products with the exact same price, within that group, our products will be sorted by thier title in descending order.
	- .filter() method returns QuerySet object.
	- QuerySets have methods called reverse. By calling this, we are actually reversing the direction of sort.
	-  query_set = Product.objects.order_by('unit_price', '-title').reverse()
	- Now unit price will be in descending order and title will be in ascending order. 
	- We can also call order_by() method after applying filter() method, as filter() method also returns a QuerySet Object and order_by() is a method of queryset.
	- query_set = Product.objects.filter(collection_id=1).order_by('unit_price)
	- product = Product.objects.order_by('unit_price')[0]
	- Above command returns an object because we are accessing the first element of our QuerySet.
	- Accessing 1st element can be done in another way: Using earliest() method. earliest() method returns an object. 
	- product = Product.objects.earliest('unit_price')
	- product = Product.objects.latest('unit_price')
	- latest() first sort the products in descending order and then returns first object.


# Limitig Results:
	- queryset = Product.objects.all()[:5]
	- Above command will return first 5 objects in the array/QuerySet at index(0, 1, 2, 3, 4)
	- queryset = Product.objects.all()[5:10]
	- Above command will return second 5 objects in the array/QuerySet at index(5, 6, 7, 8, 9)


# Selecting Certain Fields of a Table to Query:
	- Using values() we can read only certain field of objects and also related fields.
	- queryset = Product.objects.values('id', 'title', 'collection__title')
	- In values() method, instead of getting bunch of Product instances, we get bunch of dictionary objects.
	- Another method is values_list() which returns tuples instead of dictionary.
	- queryset = Product.objects.values_list('id', 'title', 'collection__title')
	- distinct(),a method  of QuerySet, used for removing similar/repeating/duplicate objects.


# Deferring Objects:
	- .only() method --> we can specify fields we want to read from our database. Similat to value() method
	- queryset = Product.objects.only('id', 'title')
	- With value() method we get dictionary objects, while with the only() method, we get instances of the product class.
	- Be CAREFUL with this method. You can end up running lots of queries.
	- Therefore, value() method is preferred.
	- defer() method --> To exclude a field(kind of) from our queryset.
	- Be careful with this too.


# Selecting Related Objects:
	- 1: select_related():
	- queryset = Product.objects.all()
	- Using above query if we also get Title of collection table (related table of Product), to find collection of each product, a separate query will run because we are only querying the Product table not the collection table or any related table. And django will not run query for collection table unless asked.
	- If we know we are going to query the related table we can preload it using select_related('TableName') method.
	- queryset = Product.objects.select_related('collection').all()
	- select_related() creates a join in our SQL query.
	- if we also want to load a table which is related to collection table, we can say:
	- select_related('1stTableName__2ndTableName')
	- we use select_related() when the other end of the relationship has one instance, like a product has one collection.
	- 2: prefetch_related():
	- we use prefetch_related() when the other end of the relationship has many instances/objects, like promotion of a product. each product have many promotions. (ManyToMany Relationship)
	- So, to preload the promotions, we'll use prefetch_related() method.
	- queryset = Product.objects.prefetch_related('promotions').all()
	- Can also call both methods together.
	- queryset = Product.objects.prefetch_related('promotions').select_related('collection').all()
	- The order for applying this method does NOT matter.


# Related Class:
	- If you make a class related to another class, yoy do NOT have to specify the relation in both class. One is enough.
	- Django will create the reverse relationship in 2nd class itslef by the name "1stClassName_set"


# Aggregation:
	- .aggregate() method. Import aggregates.
	- Product.objects.aggregate(Count('description'))
	- result = Product.objects.aggregate(count=Count('id'), min_price=Min('unit_price')) 
	- result = Product.objects.filter(collection__id=1).aggregate(count=Count('id'), min_price=Min('unit_price'))
	- aggregate() methods returns an object.


# Annotation:
	- annonate() is used to add another field/column to our table at the run time.
	- Cannot pass boolean value to annotate() method. Need to pass an expression object.
	- In django, we have an expression class which is a base class for all types of expressions.
	- In this class we have, "Value" expression for simple values, "F" for referencing fields, "Func" for calling database function (for manipualting Data), "Aggregate" (a base class for all the aggregate classes e.g., count, sum, min)
	- queryset = Customer.objects.annotate(is_new=Value(True))
	- queryset = Customer.objects.annotate(new_id=F('id'))
	- We can also perform computations in annonate() method.
	- queryset = Customer.objects.annotate(new_id=F('id') + 1)


# Calling Database Functions using Django.
	- CONCAT function of database: (Used for concatenation of string.)
	- Concatenating first and last_name of customers.
	- queryset = Customer.objects.annotate(full_name=Func(F('first_name'), Value(' '), F('last_name'), function='CONCAT'))
	- In annotate, we cannot just give any value without Value expression.
	- Another way of concatenating database.
	- queryset = Customer.objects.annotate(full_name=Concat('first_name', Value(' '), 'last_name'))
	- Concat Function takes Column name as arguments but for simple values/expression we have to give in it Value class, otherwise simple values will be taken as Column names.


# Grouping Data:
	- To look at the number of orders each customer has placed, we'll group no of orders for each customer.
	- queryset = Customer.objects.annotate(orders_count=Count('order'))
	- Here we have created customer foriegn key in order class so django creates reverse relationship in customer class as order_set. 
	- But for some reason, here 'order_set' does not work but only 'order' works.


# Expression Wrappers:
	- Expression class, a base class for all type of expressions. Derivatives of this class are:
	- Values() --> for representing simple values. e.g., boolean, number, string 
	- F() --> for referencing values
	- Func() --> for calling database functions
	- aggregate() --> a base class for all aggregate classes. e.g., count, sum, min, max etc.
	- ExpressionWrapper --> for building complex expressions.
	- queryset = Product.objects.annotate(discounted_price=F('unit_price') * 0.8)
	- Above expression raise an error. For this, we'll use ExpressionWrapper. 
	- For monetary values always use DecimalField. FloatField have rounding issues.	
	- discounted_price = ExpressionWrapper(F('unit_price') * 0.8, output_field=DecimalField())
	- queryset = Product.objects.annotate(discounted_price=discounted_price)


# Querying Generic Relationship:
	- In "tag" app, we used ContentType in class "TaggedItem" model to decouple this app from other apps in our project. It is NOT connected to other apps in the same project in anyway.
	- We can use this app anywhere other than this project too.
	- In our database, we have a table called 'django_content_type'.
	- Here we have all the models that we have defined in our apps, and some built-in django models.
	- Every model in each app have different id. can be called content_type_id.
	- Our tagged_item table have columns content_type_id and object_id.
	- Here, we can give content_type_id from the content_type table of model of any app. and as an object_id we can give any object_id of that model. An entry from that table/model.
	- For example, if we take id from the content_type table of product model of store class, and give it as content_type_id in taggedItem table of tags app, and also pick a product from the product table of store app and give its id as object id in taggedItem table of tags app.
	- In code, import ContentType class/model which contains all the models of all our apps.
	- To get our product model we can write:
	- content_type = ContentType.objects.get_for_model(Product)
	- get_for_model(), a special method for ContentType model/class.
	- Now we can find the tag for this particular product by querying TaggedItem model/table and filtering it by giving it content_type from above command and object_id (product_id of that particular product)
	- Tags should be defined in tag model of tags app.
	- So while querying, also preload Tag model.
	- queryset = TaggedItem.objects.filter(
        content_type=content_type,
        object_id=1
    )


# Custom Managers:
	- We learned this method previously:
	- content_type = ContentType.objects.get_for_model(Product)
	- queryset = TaggedItem.objects.select_related('tag').filter(
        content_type=content_type,
        object_id=1
    )

    - Another easy method: 
    - TaggedItem.objects.get_tags_for(Product, 1)
    - But for this we have to To build custom manager for the taggedItem model.	
    - "objects" attribute returns a manager, that in return help us talk to database or manage database.
    - Here we want to replace this with a custom manager.
    - This custom manager class will be created in models module in tags app. Inherited fro models.Manager class.
    - Manager class is base class for all managers.


# QuerySet Cache:
	- Reading data for a query from a database is always slower than reading it from the memory.
	- That is why when Django evaluate a query for the first time from the database, it then stores it somewhere in memory calles QuerySet cache.
	- So, 2nd time you evaluate the same query, django will not go to database again, it will read data from the QuerySet Cache.
	- for example: Here is aquery:
	- queryset = Product.objects.all()   --> Now its evaluate it. So django may run the query and connect to database.
	- list(queryset)    -- > This time django will go to database. But if we evaluate it again,
	- list(queryset)    -- > This time django will NOT go to database. It will read from QuerySet Cache.
	- Same thing happens if we acces an individual element from this queryset
	- qyeryset[0]   -- > This time again django will NOT go to database. It will read from QuerySet Cache.
	- Cache happens only if you evaluate the entire queryset first. For example, if you access an individual element from the queryset first and the read the entire queryset, you will end up sending two queries to the database.


# CREATING OBJECTS:
	- Inserting a record in the database.
	- Parent record should exist before we can create the child record. 
	- ForiegnKey or relational attribute can be given as follows:   collection ==> An object of Collection model.
	- collection.featured_product = Product(pk=1)    OR,
    - collection.featured_product_id = 1
    - after setting all the attributes, to create this object in database, you write:
    - collection.save()
    - Another way to create object is:
    - Collection.objects.create(title='a', featured_prodcut_id=1)


# Updating Objects:
	- Choose an existing object and identify it using its primary key and update its feature like this:
	- collection = Collection(pk=11)
    - collection.title = 'Games'
    - collection.featured_product = None

    - If you only update one field and does NOT include other fields while updating, django ORM will set those field's value to '', an empty string. This cause data loss.
    - It happens because when we create an object of a Model class, django ORM creates default values for all the fields of that class to either empty string or NULL

    - So, for properly update an object in Django, first we have to read it from the database, so that we have all the values in memory	then we can update it.
    - collection = Collection.objects.get(pk=11)
    - collection.featured_product = None
    - collection.save()

    - Another easy method: (But no intellisense)
    - Collection.objects.filter(pk=11).update(featured_product=None)


# Deleting Objects: 
	- Deleting single object:
	- collection = Collection(pk=11)
	- collection.delete()

	- Delete Multiple Objects:
	- To delete multiple objects, we need a queryset:
	- deleting objects whose id is greater than 5.
	- Collection.objects.filter(id__gt=5).delete()


# Transactions:
	- Sometimes we want to run multiple changes to database together so that all changes should be save togther. If one of the changes failed all changes should roll back.
	- This is where we use transaction, you wrap all the changes in the transaction and either all will committed together or if one of the operation fails, then none will bw committed. 
	- @transaction.atomic() can be used as decorator. Use this above a function and the whole function will run inside a transaction.
	- Or you can use it as a context manager using with block.
	- with transaction.atomic():
	- 	...all the changes to database...


# Executing Raw SQL Queries:
	- Sometimes querying database using django ORM can become overly complex.
	- In that case you can write SQL query by hand and execute it directly using django ORM
	- Every manager has raw method for executing raw SQL queries. 
	- It will return a queryset but this queryset will not have methods like the previous querysets have.
	- Because it does NOT make sense to have them here.

	- queryset = Product.objects.raw('SELECT * FROM store_product')

	- Use this approach only while dealing with complex queries. and it can become easy using raw SQL query or if django does NOT create your desired query using code than you should use this method.

	- Sometimes we want to run queries that don't map to our model objects, in that case we can access the database directly and bypass the model layer.
	- we connect to database directly
	- from django.db import connection
	- cursor = connection.cursor()
    - cursor.execute('SELECT * FROM store_product')
    - cursor.close()
    - Always close the cursor after executing to release the allocated resources.
    
    - Use this with "with" block. And it will close automatically
    - with connection.cursor() as cursor:
    -    cursor.execute('SELECT * FROM store_product')

