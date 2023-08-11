from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from .models import FavouriteFood # Import all models
from .forms import SignupForm


# Norman Issue 13, home page
def home(request):
    return render(request, 'users/home.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
        else:
            form = SignupForm()

        context = { 'form': form }
        return render(request, 'users/signup.html', context)


# Hello world function
# def hello_world(request):
#     grettings = "Hello"
#     return HttpResponse("Hello World" + grettings)
#
#
# # Create your views here.
# def main_page(request):
#     # Retrieve all the data from the fFavouriteFood dataset and assignes it to food_dataset
#     food_dataset = FavouriteFood.objects.all()
#     context = {'food_dataset':food_dataset}
#     return render(request, 'oms_leet/food_list.html', context)
#
#
# def user_input(request):
#     # Retrieve information from the FORM in food_list.html
#     user_name = request.GET["name"]
#     food_name = request.GET["food"]
#     food_description = request.GET["description"]
#
#     # Create an object and store it in the dataset
#     food_dataset = FavouriteFood.objects.create(username=user_name, foodName = food_name, description = food_description)
#     # Redirect to main page
#     return HttpResponseRedirect(reverse('main_page'))
