from django.contrib import admin
import datetime
from models import Restaurant, MenuItem, Reservation

class RestaurantAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class ReservationAdmi(admin.ModelAdmin):
    prepopulated_fields = {'guest_number': (datetime.datetime.now().strftime("%Y%m%d%H%M%S%f"),)}


# register the models
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(MenuItem)
admin.site.register(Reservation)