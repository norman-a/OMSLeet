"""
URL configuration for oms_leet_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from oms_leet import views # Import your app views

app_name = 'oms_leet'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello', views.hello_world, name='hello_world'), # Creates a URL for the page you want to print the first argument in the function is the URL ending, the second is the function from the views and the third the the internal variable name
    path('', views.main_page, name='main_page'), # Creates a URL for the page you want to print the first argument in the function is the URL ending, the second is the function from the views and the third the the internal variable name
    path('user_input', views.user_input, name='user_input') # Creates a URL for the page you want to print the first argument in the function is the URL ending, the second is the function from the views and the third the the internal variable name

]
