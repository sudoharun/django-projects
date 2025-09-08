from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('register', views.user_registration, name='register'),
    path('register/<user_type>', views.user_registration, name='register-with-type'),
    path('learner-registration', views.learner_registration, name='learner-registration'),
    path('tutor-registration', views.tutor_registration, name='tutor-registration'),
    path('log-in', views.log_in, name='log-in'),
    path('log-out', views.log_out, name='log-out'),

    path('create-course', views.create_course, name='create-course'),
    path('create-subject', views.create_subject, name='create-subject'),
    path('create-lesson', views.create_lesson, name='create-lesson'),
    
    path('view-course/<course_id>', views.view_course, name='view-course'),

    path('tutor-dashboard', views.tutor_view_models, name='tutor-dashboard'),

    path('learner-dashboard', views.learner_dashboard, name='learner-dashboard'),
    path('add-course-to-learner-account/<course_id>', views.add_course_to_learner_account, name='add-course-to-learner-account'),
    path('remove-course-from-learner-account/<course_id>', views.remove_course_from_learner_account, name='remove-course-from-learner-account'),

    path('admin-view-models', views.admin_view_models, name='admin-view-models'),
    path('edit-subject/<subject_id>', views.edit_subject, name='edit-subject'),
    path('delete-subject/<subject_id>/<verified>', views.delete_subject, name='delete-subject'),
    path('edit-course/<course_id>', views.edit_course, name='edit-course'),
    path('delete-course/<course_id>/<verified>', views.delete_course, name='delete-course'),
    path('edit-lesson/<lesson_id>', views.edit_lesson, name='edit-lesson'),
    path('delete-lesson/<lesson_id>/<verified>', views.delete_lesson, name='delete-lesson'),
]