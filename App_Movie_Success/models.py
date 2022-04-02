from django.db import models

# Create your models here.
class UserDetails(models.Model):
	Firstname = models.CharField(max_length = 100,default = None)
	Lastname = models.CharField(max_length = 100,default = None)
	Phone = models.CharField(max_length = 100,default = None)
	Email = models.EmailField(max_length = 100,default = None)
	Age = models.CharField(max_length = 100,default = None)
	Username = models.CharField(max_length = 100,default = None)
	Password = models.CharField(max_length = 100,default = None)
	Image = models.ImageField(upload_to = 'images',default = None)
	

	class Meta:
		db_table = 'UserDetails'


class admindata(models.Model):
    Username = models.CharField(max_length=100 ,default = None)
    Password = models.CharField(max_length=100 ,default = None)

    class Meta:
        db_table = 'admindata'


class MovieData(models.Model):
	MovieName = models.CharField(max_length = 100 , default = None)
	MovieProducer = models.CharField(max_length = 100 , default = None)
	MovieDirector = models.CharField(max_length = 100 , default = None)
	MovieWriter = models.CharField(max_length = 100,default = None)
	MovieActor = models.CharField(max_length = 100 , default = None)
	MovieActress = models.CharField(max_length = 100 , default = None)
	MovieMusic = models.CharField(max_length = 100 , default = None)
	MarketBudget = models.CharField(max_length = 100 , default = None)
	MovieGenre = models.CharField(max_length = 100,default = None)
	Day = models.CharField(max_length = 100 , default = None)
	Year = models.CharField(max_length = 100 , default = None)
	SuccessStatus = models.CharField(max_length = 100 , default = None)

	class Meta:
		db_table = 'MovieData'
