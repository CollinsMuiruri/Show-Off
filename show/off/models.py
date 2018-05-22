from django.db import models

# Create your models here.

class Location(models.Model):
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.location

class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category

class Image(models.Model):
    image_name = models.CharField(max_length =60)
    image = models.ImageField(upload_to = 'showoffimages/')
    image_description = models.TextField()
    location = models.ForeignKey(Location, null=True)
    category = models.ForeignKey(Category, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_name

    def save_image(self):
      self.save()
