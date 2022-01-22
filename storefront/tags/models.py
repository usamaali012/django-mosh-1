# Making tags app completely independet from the store class.
# tags app can be used to tag any type of object (product, video, article)
# to make this completely independent, we need to have two informations about the tagged item. Object type and Object ID. 
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
class TaggedItemManager(models.Manager):
    def get_tags_for(self, obj_type, obj_id):
        content_type = ContentType.objects.get_for_model(obj_type)
        
        queryset = TaggedItem.objects.select_related('tag').filter(
            content_type=content_type,
            object_id=obj_id
        )

        return queryset


class Tag(models.Model):
    label = models.CharField(max_length=255)


class TaggedItem(models.Model):
    objects = TaggedItemManager()
    # What tag is applied to what object
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField() 
    content_object = GenericForeignKey()
