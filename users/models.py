from django.db import models

class Stopien(models.Model):
	name = models.CharField(max_length = 1)
	semestr = models.CharField(max_length = 1)
	def __str__(self):
		return "{name} semestr: {semestr}".format(name=self.name, 
			semestr=self.semestr)

class Kierunek(models.Model):
	name = models.CharField(max_length = 50)
	yearbased = models.CharField(max_length = 4)
	stopien = models.ForeignKey(Stopien)
	def __str__(self):
		return "{name} yearbase: {yearbase}".format(name=self.name, 
			yearbase=self.yearbase)

class Wydzial(models.Model):
	cod = models.CharField(max_length = 5)
	name = models.CharField(max_length = 50)
	kierunek = models.ForeignKey(Kierunek)
	def __str__(self):
		return "{cod} nazwa: {name}".format(cod=self.cod, 
			name=self.name)





class User(models.Model):
	userID = models.CharField(max_length = 10)
	first_name = models.CharField(max_length = 100)
	sur_name = models.CharField(max_length = 100)
	eMail = models.CharField(max_length = 50)
	password = models.CharField(max_length = 50)
	wydzial = models.ForeignKey(Wydzial)
	def __str__(self):
		return "{userID} first_name: {first_name}, sur_name: {sur_name}".format(userID=self.userID, first_name=self.first_name, sur_name=self.sur_name)
	

