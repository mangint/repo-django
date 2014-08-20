from django.db import models

# Create your models here.

class School (models.Model):
	name = models.CharField(max_length=50)
	country = models.CharField(max_length=50)
#	number_of_students = models.DecimalField()
#	current_students = models.ForeignKey(Student)
	def __str__(self):
		return self.name, self.country

class Student (models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	school= models.ForeignKey(School)
	def __str__(self):
		return (self.name , self.last_name)