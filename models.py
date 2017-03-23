from django.db import models
from datetime import datetime

class PersonInfo(models.Model):
    rollNo = models.TextField(max_length=20,primary_key = True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.TextField(max_length=70)
    email = models.EmailField(max_length=30)
    phoneNo = models.IntegerField(max_length=10)

	

class AcedamicInfo(models.Model):
	studentId = models.ForeignKey(PersonInfo, on_delete=models.CASCADE)
	yearOfJoining = models.IntegerField(max_length=30)
	aggregate = models.IntegerField(max_length=30)
	upperSecondaryInstitution = models.CharField(max_length=70)
	upperSecondaryBoard = models.CharField(max_length=30)
	upperSecondaryPercentage = models.IntegerField(max_length=10)
	SecondaryPercentage = models.IntegerField(max_length=10)
	SecondaryInstitution = models.CharField(max_length=10)
	SecondaryBoard = models.CharField(max_length=10)

class AdditionalInfo(models.Model):
	studentId = models.ForeignKey(PersonInfo, on_delete=models.CASCADE)
	coAcademicActivities = models.CharField(max_length=30)
	details = models.TextField(max_length=30)
	coCurriculars = models.CharField(max_length=30)
	hobbies = models.CharField(max_length=30)

class Notifications(models.Model):
	driveName = models.ForeignKey(PersonInfo, on_delete=models.CASCADE)
	
	date = models.TextField()
	notification = models.CharField(max_length=30)
	