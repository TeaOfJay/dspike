from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .models import Course, Profile, Assignment, CourseComment, AssignmentComment
from django.contrib.auth.models import User
from .forms import ProfileUpdateForm, CourseCreateForm, AssignmentCreateForm, CourseCommentCreateForm, AssignmentCommentCreateForm

from .models import current_semester, current_year
class CourseListView(generic.ListView):
	model = Course
	paginate_by = 10
	template_name='ratem/course_list.html'
	def get(self, request, *args, **kwargs):
		courses = Course.objects.all()
		return render(request, 'ratem/course_list.html', {'courses':courses})


class RegisterView(generic.CreateView):
	form_class=UserCreationForm
	success_url=reverse_lazy('login')
	template_name='ratem/register.html'

class CourseView(generic.DetailView):
	model = Course
	template_name='ratem/coursedetail.html'


class ProfileView(generic.DetailView):
	model = Profile
	template_name='ratem/profiledetail.html'

	def get(self, request, *args, **kwargs):

		user = User.objects.get(pk=kwargs['pk'])
		#current = user.courses.filter(year=current_year, semester=current_semester)
		self.kwargs = kwargs
		profile = user.profile
		current = profile.courses.filter(year=current_year(), semester=current_semester())
		past    = profile.courses.exclude(year=current_year(), semester=current_semester())
		context = {'profile':profile, 'current': current, 'past':past}
		return render(request, self.template_name, context)

class ProfileUpdateView(generic.UpdateView):
	model=Profile
	form_class = ProfileUpdateForm
	#fields=['first_name', 'last_name']
	template_name='ratem/profileupdate.html'
	
	def get_success_url(self, **kwargs):
		if self.kwargs != None:
			return reverse_lazy('profile-detail', kwargs = {'pk' : self.kwargs['pk']})
		return reverse_lazy('course-list')


	
class CourseDetailView(generic.DetailView):
	model=Course
	template_name='ratem/course_detail.html'
	def get(self, request, *args, **kwargs):

		course = Course.objects.get(pk=kwargs['pk'])
		assignments = course.assignments.all()
		comments = course.comments.all()

		context = {'course':course, 'assignments': assignments, 'comments': comments}
		return render(request, self.template_name, context)

class CourseCreateView(generic.CreateView):
	model=Course
	form_class = CourseCreateForm
	success_url = reverse_lazy('course-list')
	template_name = 'ratem/course_create.html'
class AssignmentDetailView(generic.DetailView):
	model=Assignment
	template_name='ratem/assignment_detail.html'
	def get(self, request, *args, **kwargs):

		
		assignment = Assignment.objects.get(pk=kwargs['apk'])
		course = assignment.course
		comments = assignment.comments.all()
		context = {'course': course, 'assignment': assignment, 'comments': comments}
		return render(request, self.template_name, context)


class AssignmentCreateView(generic.CreateView):
	model=Assignment
	form_class = AssignmentCreateForm
	template_name = 'ratem/assignment_create.html'
	def get_success_url(self, **kwargs):
		if self.kwargs != None:
			return reverse_lazy('course-detail', kwargs = {'pk' : self.kwargs['pk']})
		return reverse_lazy('course-list')
	def form_valid(self, form):
		form.instance.course = Course.objects.get(pk=self.kwargs['pk'])
		return super().form_valid(form)
'''
	def get(self, request, *args, **kwargs):
		self.kwargs = kwargs
		return super().get(self, request, args, kwargs)
'''

class CourseCommentCreateView(generic.CreateView):
	model = CourseComment
	form_class = CourseCommentCreateForm
	template_name = 'ratem/course_comment_create.html'
	def get_success_url(self, **kwargs):
		if self.kwargs != None:
			return reverse_lazy('course-detail', kwargs = {'pk' : self.kwargs['pk']})
		return reverse_lazy('course-list')
	def form_valid(self, form):
		form.instance.course = Course.objects.get(pk=self.kwargs['pk'])
		return super().form_valid(form)
class AssignmentCommentCreateView(generic.CreateView):
	model=AssignmentComment
	form_class = AssignmentCommentCreateForm
	template_name = 'ratem/assignment_comment_create.html'
	def get_success_url(self, **kwargs):
		if self.kwargs != None:
			return reverse_lazy('assignment-detail', kwargs={'pk':self.kwargs['pk'], 'apk':self.kwargs['apk']})
		return reverse_lazy('course-list')
	def form_valid(self, form):
		form.instance.course = Course.objects.get(pk=self.kwargs['pk'])
		form.instance.assignment = Assignment.objects.get(pk=self.kwargs['apk'])
		return super().form_valid(form)