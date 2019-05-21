from django.db import models

# Create your models here.

class Blog(models.Model):
    name = models.CharField(max_length=20)    
    date = models.DateField('date')    
    message = models.TextField()

    def __str__(self):
        return self.name