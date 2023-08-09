from django.db import models

# Create your models here.
class FavouriteFood(models.Model):
    username = models.CharField(max_length=50)
    foodName = models.CharField(max_length=50)
    description = models.TextField()
    

    def __str__(self):
        return self.username + self.description