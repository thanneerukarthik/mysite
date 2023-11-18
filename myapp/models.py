from django.db import models

class Item(models.Model):
     
    name = models.CharField(max_length=100)
    # description = models.TextField()

    def __str__(self):
        return self.name

 # myapp/models.py

from django.db import models

class Item(models.Model):
    # your model fields here

    class Meta:
        app_label = 'myapp'
