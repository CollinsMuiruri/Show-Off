from django.test import TestCase
from models import Location, Image


# Create your tests here.
class LocationTestClass(TestCase):

    def setUp(self):
        # creating a new Location and saving the Location
        self.new_location = Image(image_NAME='name', image='gif.png')
        self.new_location.save_location()

    def tearDown(self):
        Location.objects.all().delete()
