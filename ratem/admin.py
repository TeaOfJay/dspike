from django.contrib import admin
from .models import Course, Assignment, CourseComment, AssignmentComment, Profile
# Register your models here.

admin.site.register(Course)
admin.site.register(Assignment)
admin.site.register(CourseComment)
admin.site.register(AssignmentComment)
admin.site.register(Profile)