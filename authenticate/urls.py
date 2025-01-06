from django.contrib import admin
from django.urls import path, include
from authenticate import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('', views.home, name='home'),
    path('submit-request/', views.submit_request, name='submit_request'),
    path('create-course/', views.create_course, name='create_course'),
    path('track-progress/', views.track_progress, name='track_progress'),
    path('my-progress/',views.my_progress, name='my_progress'),
    path('mark-module-completed/<int:module_id>/', views.mark_module_completed, name='mark_module_completed'),
    path('generate-cred/',views.generate_cred, name='generate_cred'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('manager-dashboard/', views.manager_dashboard, name='manager_dashboard'),
    path('employee-dashboard/', views.employee_dashboard, name='employee_dashboard'),
    path('view-requests/', views.view_requests, name='view_requests'),
    path('view-courses/', views.view_courses, name='view_courses'),
    path('view-course-details/<int:course_id>/', views.view_course_details, name='view_course_details'),
    path('my-requests/', views.my_requests, name='my_requests'),
    path('delete-request/<int:request_id>/', views.delete_request, name='delete_request'),
    path('delete-course/<int:course_id>/', views.delete_course, name='delete_course'),
    path('submit-request/', views.submit_request, name='submit_request'),
    path('admin-requests/', views.admin_requests, name='admin_requests'),
    path('handle-request/<int:request_id>/', views.handle_request, name='handle_request'),
    path('submit-feedback/', views.submit_feedback, name='submit_feedback'),
    path('view-feedback/', views.view_feedback, name='view_feedback'),
    path('view-notifications/', views.view_notifications, name='view_notifications'),
    path('notifications/mark_as_read/<int:course_id>/', views.mark_as_read, name='mark_as_read'),
    path('course/<int:course_id>/add_emails/', views.add_employee_emails, name='add_employee_emails'),
]






   



   
    
