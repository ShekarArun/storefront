from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Tag(models.Model):
    label = models.CharField(max_length=255)


class TaggedItem(models.Model):
    # Indicates which tag is applied to which object (Independent of specific type of object it is applied to)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    # Associate generic type of content with tag, so anything can be related to it
    # To identify this, we need 2 pieces of information - the object type to which the tag is associated, and a unique ID for that object
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
