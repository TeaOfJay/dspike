from django.db import models
from django.contrib.auth.models import User
import datetime

#User models

SPRING = 0
SUMMER = 1
FALL = 2

SEMESTER_CHOICES = (
		(SPRING, 'Spring'), 
		(SUMMER, 'Summer'),
		(FALL, 'Fall')
	)

'''
class Semester(models.Model):
	def current_year(self):
		return datetime.datetime.now().year

	semester = models.IntegerField(choices=SEMESTER_CHOICES, default=SPRING)
	year     = models.IntegerField(default=current_year)
'''
def current_semester():
		t = datetime.datetime.today()
		if t.month < 5:
			return SPRING
		elif t.month < 9:
			return SUMMER
		return FALL
def current_year():
	return datetime.datetime.today().year

class Course(models.Model):
	#subject = models.CharField(max_length=20)
	#course_number = models.IntegerField()
	name = models.CharField(max_length=100)
    
	description = models.TextField()
	gpa = models.DecimalField(decimal_places=2, max_digits=3)
	rating = models.DecimalField(decimal_places=2, max_digits=3)
	semester = models.IntegerField(choices=SEMESTER_CHOICES, default=current_semester)
	year     = models.IntegerField(default=current_year)


	def __str__(self):
		return self.name

class Assignment(models.Model):
	name = models.CharField(max_length=255)#
	description = models.TextField()
	course = models.ForeignKey(to=Course, related_name="assignments", on_delete=models.CASCADE)
	#rating
	def __str__(self):
		return self.name


class CourseComment(models.Model):
	title   = models.CharField(max_length=255)
	comment = models.TextField()
	course  = models.ForeignKey(to=Course, related_name="comments", on_delete=models.CASCADE)
class AssignmentComment(models.Model):
	title      = models.CharField(max_length=255)
	comment    = models.TextField()
	assignment = models.ForeignKey(to=Assignment, related_name="comments", on_delete=models.CASCADE)



UNDERGRADUATE = 0
GRADUATE      = 1
POSTGRADUATE  = 2
DEGREE_CHOICES = (
		(UNDERGRADUATE, 'Undergraduate'), 
		(GRADUATE, 'Graduate'),
		(POSTGRADUATE, 'Postgraduate')
	)


class Profile(models.Model):
	owner = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE, primary_key=True)

	first_name = models.CharField(max_length=40, blank=True)
	last_name  = models.CharField(max_length=40, blank=True)
	school     = models.CharField(max_length=20, blank=True)
	major      = models.CharField(max_length=30, blank=True)
	degree     = models.IntegerField(choices=DEGREE_CHOICES, default=UNDERGRADUATE)
	courses = models.ManyToManyField(Course, related_name="students")
