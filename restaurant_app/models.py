from django.db import models
from django.template.defaultfilters import slugify
import datetime


class Restaurant(models.Model):
    name = models.CharField(max_length=128, unique=True)
    address = models.CharField(max_length=150)
    telephone = models.CharField(max_length=128, unique=True)
    photo_link = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Restaurant, self).save(*args, **kwargs)



class MenuItem(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=255)
    price = models.CharField(max_length=40)
    course = models.CharField(max_length=60)
    restaurant = models.ForeignKey(Restaurant)


    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

def set_defualt_reservation_date():
    # default date is one day after the date of reservation
    return datetime.date.today()+datetime.timedelta(days=1)

def set_default_guest_number():
    # guest number is the datetime converted to string
    return datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")

class Reservation(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    reservation_date = models.DateField(default=set_defualt_reservation_date, unique=False)
    phone_number = models.CharField(max_length=128)
    guest_number = models.CharField(unique=True, max_length=128, default=set_default_guest_number)
    email = models.EmailField(max_length=128)
    comment = models.CharField(max_length=200)
    restaurant = models.ForeignKey(Restaurant)

    def __str__(self):
        return self.first_name + self.last_name

    def __unicode__(self):
        return self.first_name + self.last_name





