from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import User

class UserListView(ListView):
	model = User
	
