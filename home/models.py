from django.db import models


# Create your models here.
class Contact(models.Model):
    name=models.CharField( max_length=50)
    email=models.EmailField()
    subject=models.CharField(max_length=50)
    message=models.TextField()

    def __str__(self):
        return self.name


class Index(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title

class Career(models.Model):
    notice = models.CharField(max_length = 200 , blank=True)
    title = models.CharField(max_length = 200, blank=True)
    title_tag = models.CharField(max_length = 200, blank=True)
    title_butt = models.CharField(max_length = 200 , blank=True)
    contents = models.TextField(blank=True)
    img = models.ImageField(upload_to="static/img/", blank=True) 
    
    def __str__(self):
        return self.title

class About(models.Model):
    title= models.CharField(max_length=200)
    img = models.ImageField(upload_to="static/img/") 


class Training(models.Model):
    title= models.CharField(max_length=200)
    contents = models.TextField(blank=True)

    def __str__(self):
        return self.title