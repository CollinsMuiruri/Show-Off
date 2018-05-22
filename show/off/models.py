from django.db import models

# Create your models here.

class Location(models.Model):
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.location

class Category(models.Model):
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.category

class Image(models.Model):
    image = models.ImageField(upload_to = 'articles/')
    image_name = models.CharField(max_length =60)
    image_description = models.TextField()
    location = models.ForeignKey(Location)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image
