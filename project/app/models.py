from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db import models  # ✅ ONLY THIS

class Teams(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Teams'

    def __str__(self):
        return self.name
    

class Sports(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Sports'

    def __str__(self):
        return self.name

class Nationalities(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Nationalities'

    def __str__(self):
        return self.name






class Players(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='player_photos/')
    date_of_birth = models.DateField()
    nationality = models.ForeignKey(Nationalities, on_delete=models.CASCADE)
    team = models.ForeignKey(Teams, on_delete=models.CASCADE)
    sports = models.ForeignKey(Sports, on_delete=models.CASCADE)


class UserPredictModel(models.Model):
    image = models.ImageField(upload_to = 'images/')
    label = models.CharField(max_length=20,default='data')

    def __str__(self):
        return str(self.image)
    


from django.db import models

class Patient_info(models.Model):
    Country = models.FloatField()  # Example: consider using choices=(...) for gender
    CapStatus = models.FloatField()
    Innings = models.FloatField()
    Runs = models.FloatField()  # Example: consider using BooleanField for binary fields
    Balls = models.FloatField()
    Average = models.FloatField()
    SR = models.FloatField()
    Fifites = models.FloatField()
    hundreds = models.FloatField()
    Fours = models.FloatField()
    Sixes = models.FloatField()
    Notout = models.FloatField()
    PlayerRole = models.FloatField()

    Class = models.CharField(max_length=100)

    def __str__(self):
        return f"Prediction: {self.Class}"
    

from django.db import models

class Patient_info1(models.Model):
    Specialism = models.FloatField()  # Example: consider using choices=(...) for gender
    Innings = models.FloatField()
    Avg = models.FloatField()
    SR = models.FloatField()  # Example: consider using BooleanField for binary fields
    Fifties = models.FloatField()
    Hundreds = models.FloatField()
    Fours = models.FloatField()
    Sixes = models.FloatField()
    Runs = models.FloatField()
    Balls = models.FloatField()
    NotOuts = models.FloatField()

    Class = models.CharField(max_length=100)

    def __str__(self):
        return f"Prediction: {self.Class}"