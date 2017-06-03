# set the environment and point to the setting module
import os
from restaurant.settings import BASE_DIR

os.environ['DJANGO_SETTINGS_MODULE'] = 'restaurant.settings'



from restaurant_app.models import Restaurant, MenuItem

RESTAURANTS = {
    'Mamba Point Lagoonda': {
        'name': "Mamba Point Lagoonda",
        'address': '53 Cape Road, Off Aberdeen Road, Freetown',
        'telephone': '+23299100100',
        'photo_link': os.path.join(BASE_DIR, "restaurant_app/static/images/mamba_point.jpg"),
        },
    'Crown Xpress': {
        'name': "Crown Xpress",
        'address': '125 Wilkinson Road, Freetown',
        'telephone': '+23278999222',
        'photo_link': os.path.join(BASE_DIR, "restaurant_app/static/images/crown_xpress.jpg"),
        },
    "Gina's": {
        'name': "Gina's",
        'address': '125 Wilkinson Road, Freetown',
        'telephone': '+23277919999',
        'photo_link': os.path.join(BASE_DIR, "restaurant_app/static/images/ginas.jpg")
        },
}

MENU_ITEMS = {
    'Rice and cassava leaves': {
        'name': 'Rice and cassava leaves',
        'description': 'Cassava leaves cooked with fish and palm oil. Served with rice',
        'price': 'Le 300,000.00',
        'course': 'Main',
        'restaurant': Restaurant(id=2)

    }
}

def populate_restaurant_table(restaurants_dict):
    for name, restaurant in restaurants_dict.items():
        rest_obj = Restaurant()
        rest_obj.name = restaurant.get('name')
        rest_obj.address = restaurant.get('address')
        rest_obj.telephone = restaurant.get('telephone')
        rest_obj.photo_link = restaurant.get('photo_link')
        rest_obj.save()
        print rest_obj.name, 'saved'


def populate_menu_items(menu_items_dict):
    for name, menu_item in menu_items_dict.items():
        menu_obj = MenuItem()
        menu_obj.name = menu_item.get('name')
        menu_obj.name = menu_item.get('name')
        menu_obj.description = menu_item.get('description')
        menu_obj.price =menu_item.get('price')
        menu_obj.course = menu_item.get('course')
        menu_obj.restaurant = menu_item.get('restaurant')
        menu_obj.save()
        print menu_obj.name, 'saved'

if __name__ == '__main__':
    #populate_restaurant_table(RESTAURANTS)
    populate_menu_items(MENU_ITEMS)
