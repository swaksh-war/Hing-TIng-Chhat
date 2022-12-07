from django.db import models

# Create your models here.
class Blog(models.Model):
    Author = models.CharField(max_length=255, default='Subrata Kr Paul')
    Title = models.CharField(max_length=500, blank=True)
    description = models.TextField(max_length=4000)
    picture = models.FileField(upload_to='uploads')
    uploaded_date = models.DateTimeField(auto_now_add= False) 

    def __str__(self):
        return self.Title

class Subscriber(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=False)
    number = models.IntegerField(max_length=11)

    def __str__(self):
        return self.name