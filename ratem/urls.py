"""
"""
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
	path('', views.CourseListView.as_view(), name='index'),
	path('courses/', views.CourseListView.as_view(), name='course-list'),
	path('courses/<int:pk>/', views.CourseDetailView.as_view(), name='course-detail'),
	path('courses/<int:pk>/comments/update', views.CourseCommentCreateView.as_view(), name='course-comment-create'),
	path('courses/update/', views.CourseCreateView.as_view(), name='course-create'),
	path('courses/<int:pk>/assignments/<int:apk>/', views.AssignmentDetailView.as_view(), name='assignment-detail'),
	path('courses/<int:pk>/assignments/update/', views.AssignmentCreateView.as_view(), name='assignment-create'),
	path('courses/<int:pk>/assignments/<int:apk>/comments/update', views.AssignmentCommentCreateView.as_view(), name='assignment-comment-create'),
	path('register/', views.RegisterView.as_view(), name='register'),
	path('users/<int:pk>/', views.ProfileView.as_view(), name='profile-detail'),
	path('users/<int:pk>/update_profile', views.ProfileUpdateView.as_view(), name='profile-update')


	#path('', views.courses)
    #path('courses/', views.courses, name='courses'),
    #
    #path('<username>/', views.user, name='user'),
    #path('<course>')
]
