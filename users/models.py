from django.db import models

class Stopien(models.Model):
	name = models.CharField(max_length = 1)
	semestr = models.CharField(max_length = 1)

class Kierunek(models.Model):
	name = models.CharField(max_length = 50)
	yearbased = models.CharField(max_length = 4)
	stopien = models.ForeignKey(Stopien)

class Wydzial(models.Model):
	cod = models.CharField(max_length = 5)
	name = models.CharField(max_length = 50)
	kierunek = models.ForeignKey(Kierunek)





class User(models.Model):
	name = models.CharField(max_length = 100)
	eMail = models.CharField(max_length = 50)
	password = models.CharField(max_length = 50)
	wydzial = models.ForeignKey(Wydzial)
	

