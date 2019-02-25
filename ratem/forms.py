from django import forms
from .models import Profile, Assignment, Course, CourseComment, AssignmentComment


class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('first_name', 'last_name', 'school', 'major', 'degree', 'courses')

class CourseCreateForm(forms.ModelForm):
	class Meta:
		model = Course
		fields = ('name', 'description', 'gpa', 'rating', 'semester', 'year')

class AssignmentCreateForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(AssignmentCreateForm, self).__init__(*args, **kwargs)
		#if kwargs is not None and 'pk' in kwargs:
		#	self.fields['course']=Course.objects.get(pk=kwargs['pk'])
		#self.fields['course'].disabled=True
	class Meta:
		model = Assignment
		fields = ('name', 'description')

class CourseCommentCreateForm(forms.ModelForm):
	class Meta:
		model = CourseComment
		fields = ('title', 'comment')

class AssignmentCommentCreateForm(forms.ModelForm):
	class Meta:
		model = AssignmentComment
		fields = ('title', 'comment')