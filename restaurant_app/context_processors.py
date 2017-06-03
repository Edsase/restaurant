from .forms import ReservationForm
import views

# context processor data will be available on to all templates
def reservation_form_handler(request):
    "function displays and updates db with info filled into the form"
    reservation_form = ReservationForm()

    # a http post?
    if request.method == "POST":
        form = ReservationForm(request.POST)
        # check if form has been validly filled out
        if form.is_valid():
            # save the new reservation request
            form.save(commit=True)
            # send request to redirect page
            # use homepage for redirection
            return views.show_restaurant_menu(request)
        else:
            # there are errors in the form
            print form.errors
    # render the form with error messages if any
    return {'reservation_form': reservation_form}