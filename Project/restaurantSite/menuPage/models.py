from django.db import models

# Create your models here.
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    # Define other fields as needed

    # Mayhaps needed?!
    # class Meta:
    #     app_label = 'your_app_label'