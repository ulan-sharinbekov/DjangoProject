from django.db import models

# Create your models here.
class Club(models.Model):
    title = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    year = models.IntegerField(default=2002)
    budget = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.title, self.country, self.year, self.budget}'


class Footballer(models.Model):
    firstname = models.CharField(max_length=200)
    surename = models.CharField(max_length=200)
    age = models.IntegerField(default=20)
    clube = models.ForeignKey(Club, on_delete=models.CASCADE, related_name="get_clube")


    def __str__(self):
        return f'{self.firstname, self.surename, self.age, self.clube}'
