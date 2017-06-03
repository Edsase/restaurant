from django import template

from restaurant_app.models import Reservation

register = template.Library()

@register.inclusion_tag('restaurant_app/reservation_form.html')
def get_reservation_details():
    return {'reservation_details': Reservation.objects.all()}
