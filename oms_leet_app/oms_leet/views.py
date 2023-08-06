from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import FavouriteFood # Import all models

# Hello world function
def hello_world(request):
    grettings = "Hello"
    return HttpResponse("Hello World" + grettings)

# Create your views here.
def main_page(request):
    # Retrieve all the data from the fFavouriteFood dataset and assignes it to food_dataset
    food_dataset = FavouriteFood.objects.all()
    context = {'food_dataset':food_dataset}
    return render(request, 'oms_leet/food_list.html', context)

def user_input(request):
    # Retrieve information from the FORM in food_list.html
    user_name = request.GET["name"]
    food_name = request.GET["food"]
    food_description = request.GET["description"]

    # Create an object and store it in the dataset
    food_dataset = FavouriteFood.objects.create(username=user_name, foodName = food_name, description = food_description)
    # Redirect to main page
    return HttpResponseRedirect(reverse('main_page'))
