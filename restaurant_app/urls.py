from django.conf.urls import url
from restaurant_app import views

# make url patterns for this app
app_name = 'restaurant_app'
urlpatterns = [
    url(r"^$", views.index, name='index'),
    url(r'(?P<restaurant_name_slug>[\w\-]+)/$', views.show_restaurant_menu, name='show_restaurant_menu'),
    url(r"about$", views.about, name="about"),

]