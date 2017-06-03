from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
# import the models
from .models import Restaurant, MenuItem
# import forms
from .forms import ReservationForm


def index(request):
    """
        view to display list of restaurants in the db
        :param request: 
        :return: 
        """
    restaurants_list = Restaurant.objects.order_by('name')
    context_dict = {"restaurants": restaurants_list}
    return render(request, 'restaurant_app/index.html', context_dict)

def reservation_form_handler(request, restaurant_name_slug):
    "function displays and updates db with info filled into the form"
    # a http post?
    if request.method == "POST":
        form = ReservationForm(request.POST)

        # check if form has been validly filled out
        if form.is_valid():
            # save the new reservation request
            print "form is valid"
            form.save(commit=True)
            # send request to redirect page
            # use homepage for redirection
            url = reverse('restaurant_app:show_restaurant_menu', args=(restaurant_name_slug,))
            return HttpResponseRedirect(url)
        else:
            # there are errors in the form
            print form.errors
    else:
        form = ReservationForm()
    # render the form with error messages if any
    print "did not handle form"
    url = reverse('restaurant_app:show_restaurant_menu', args=(restaurant_name_slug,))
    return HttpResponseRedirect(url)

def reservation_confirmation(request, restaurant_name_slug, reservation):
    """
    displays page to confirm reservation
    :param request: 
    :return: 
    """
    pass


def show_restaurant_menu(request, restaurant_name_slug):
    """
    view to display menu items of a given restaurant
    :param request: 
    :return: 
    """
    context_dict = {}
    try:
        # retrieve the name of the restuarant whose menu_items is to be displayed
        restaurant = Restaurant.objects.get(slug=restaurant_name_slug)
        # retrieve all the menu items in that restaurant
        menu_items = MenuItem.objects.filter(restaurant=restaurant)
        # add result list to the context dict
        context_dict['menu_items'] = menu_items
        context_dict['restaurant'] = restaurant
        if request.method == 'POST':
            form = ReservationForm(request.POST)
            # check if form has been validly filled out
            if form.is_valid():
                # save the new reservation request
                print "form is valid"
                form.save(commit=True)
                # send request to redirect page
                # use homepage for redirection
                url = reverse('restaurant_app:show_restaurant_menu', args=(restaurant_name_slug,))
                return HttpResponseRedirect(url)
            else:
                # there are errors in the form
                print form.errors
        else:
            context_dict['form'] = ReservationForm()

    except Restaurant.DoesNotExist:
        # do pass anything
        context_dict['menu_items'] = None
        context_dict['restaurant'] = None
    template_to_render = 'restaurant_app/restaurant/' + restaurant_name_slug + '.html'
    return render(request, template_to_render, context_dict)




def add_menu(request):
    """
    view to add a new menu item
    :param request: 
    :return: 
    """

    return HttpResponse("This page will all you to add menus")

def about(request):
    """
    view for about page
    :param request: 
    :return: 
    """
    response = ""
    response += "This is the about page!"
    response += "<a href=%s>Back to restaurants</a>" %"restaurants/list_of_restaurants"
    return HttpResponse(response)



