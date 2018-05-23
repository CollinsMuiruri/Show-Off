from django.db import models
import datetime as dt

# Create your models here.


class Location(models.Model):
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.location

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    @classmethod
    def filter_by_location(cls, location):
        images = cls.objects.filter(location)
        return images


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    @classmethod
    def search_by_title(cls, search_term):
        images = cls.objects.filter(category__icontains=search_term)
        return images

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()


class Image(models.Model):
    image_name = models.CharField(max_length=60)
    image = models.ImageField(upload_to='showoffimages/')
    image_description = models.TextField()
    location = models.ForeignKey(Location, null=True)
    category = models.ForeignKey(Category, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_name

    @classmethod
    def latest_showoffs(cls):
        today = dt.date.today()
        images = cls.objects.filter(pub_date__date=today)
        return images

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self):
        self.update()

    def get_image_by_id(cls, id):
        pass
