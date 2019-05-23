from django.db import models

# Create your models here.

class Blog(models.Model):
    name = models.CharField(max_length=15)   
    date = models.DateField('date')    
    message = models.TextField()

    def __str__(self):
        return self.name
    def summary(self):
        return self.message[:25]