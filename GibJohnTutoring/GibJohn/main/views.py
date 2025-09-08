from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, LoginForm, SubjectForm, CourseForm, LessonForm
from django.contrib.auth.decorators import permission_required, login_required, user_passes_test
from .models import Learner, Tutor, Subject, Course, Lesson

# Other functions

def is_superuser(user):
    return user.is_superuser

def get_full_name(user):
    return user.first_name + " " + user.last_name

def homepage(request):
    courses = Course.objects.all()
    subjects = Subject.objects.all()

    context = {
        "courses": courses,
        "subjects": subjects,
    }

    return render(request, 'homepage.html', context)

def view_course(request, course_id):
    learner = None
    course_in_account = False
    
    course = Course.objects.get(pk=course_id)
    lessons = course.lessons.all()
    if request.user.is_authenticated:
        try:
            learner = Learner.objects.get(user=request.user)
            if learner in course.learners.all():
                course_in_account = True
        except:
            pass

    context = {
        "course": course,
        "lessons": lessons,
        "course_in_account": course_in_account
    }
    return render(request, 'view_course.html', context)

# Registration-related views

def user_registration(request, user_type=None):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "GET":
        form = CustomUserCreationForm()
    else:
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            if user_type == "tutor":
                Tutor.objects.create(user=user)
            else:
                Learner.objects.create(user=user)

            login(request, user)
            messages.success(request, 'Registered successfully!')
            return redirect('home')

    if user_type is None:
        user_type = 0

    context = {
        "form": form,
        "user_type": user_type,
        "tutor": "tutor",
        "learner": "learner",
    }

    return render(request, 'register.html', context)

def learner_registration(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Learner.objects.create(user=user)
            login(request, user)
            messages.success(request, 'Registered successfully!')
            return redirect('home')

    messages.error(request, "There was an unknown error!")
    return redirect('home')

def tutor_registration(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Tutor.objects.create(user=user)
            login(request, user)
            messages.success(request, 'Registered successfully!')
            return redirect('home')
    
    messages.error(request, "There was an unknown error!")
    return redirect('home')

# Logging in/out views

def log_in(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "GET":
        form = LoginForm()
        return render(request, 'login.html', {"form": form})
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Successfully logged in as {username}!")
            else:
                messages.error(request, "There was a problem logging you in!")

    return redirect('home')

def log_out(request):
    if request.user.is_authenticated:
        logout(request)
        
    return redirect('home')

# Tutor/superuser views for course manipulation

@login_required
@permission_required('main.can_view_tutor_dashboard', raise_exception=True)
def tutor_view_models(request):
    tutor = Tutor.objects.get(user=request.user)
    courses = tutor.courses.all()
    lessons = tutor.lessons.all()

    context = {
        "courses": courses,
        "lessons": lessons,
    }
    return render(request, 'tutor_dashboard.html', context)

@login_required
@permission_required('main.can_create_own_course', raise_exception=True)
def create_course(request):
    if request.method == "GET":
        form = CourseForm()
        return render(request, 'create_course.html', {"form": form})
    else:
        form = CourseForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            if request.user.tutor:
                course = form.save(commit=False)
                tutor = Tutor.objects.get(user=request.user)
                course.author = tutor
                course.save()
            else:
                form.save()
            messages.success(request, f"Successfully created the {title} course!")

    if request.user.is_superuser:
        return redirect('admin-view-models')
    else:
        return redirect('tutor-dashboard')

# Tutor/superuser views for lesson manipulation

@login_required
@permission_required('main.can_create_own_lesson', raise_exception=True)
def create_lesson(request):
    if request.method == "GET":
        form = LessonForm()
        return render(request, 'create_lesson.html', {"form": form})
    else:
        form = LessonForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            try:
                course = form.save(commit=False)
                tutor = Tutor.objects.get(user=request.user)
                course.author = tutor
                course.save()
            except:
                form.save()
            messages.success(request, f"Successfully created the {title} lesson!")

    if request.user.is_superuser:
        return redirect('admin-view-models')
    else:
        return redirect('tutor-dashboard')

# superuser views for viewing/editing/deleting subjects/courses/lessons

# superuser view for viewing all models

@user_passes_test(is_superuser)
def admin_view_models(request):
    subjects = Subject.objects.all()
    courses = Course.objects.all()
    lessons = Lesson.objects.all()

    context = {
        "subjects": subjects,
        "courses": courses,
        "lessons": lessons,
    }
    return render(request, 'admin_view_models.html', context)

# superuser views relating to subjects

# superuser views for creating subjects

@user_passes_test(is_superuser)
def create_subject(request):
    if request.method == "GET":
        form = SubjectForm()
        return render(request, 'create_subject.html', {"form": form})
    else:
        form = SubjectForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            form.save()
            messages.success(request, f"Successfully created the {title} subject!")

    return redirect('admin-view-models')

@user_passes_test(is_superuser)
def edit_subject(request, subject_id):
    instance = Subject.objects.get(pk=subject_id)

    if request.method == "POST":
        form = SubjectForm(request.POST, instance=instance)

        if form.is_valid():
            form.save()

            title = form.cleaned_data["title"]
            messages.success(request, f"Successfully edited {title} subject!")
            return redirect("admin-view-models")
    else:
        form = SubjectForm(instance=instance)

    return render(request, "edit_subject.html", {"form": form})

@user_passes_test(is_superuser)
def delete_subject(request, subject_id, verified=-1):
    if int(verified) >= 0:
        if int(verified) == 1:
            instance = Subject.objects.get(pk=subject_id)
            title = instance.title
            instance.delete()
            messages.success(request, f"Successfully deleted {title} subject")
            return redirect('admin-view-models')
        else:
            instance = Subject.objects.get(pk=subject_id)
            title = instance.title
            messages.error(request, f"Unable to delete {title} subject!")
            return redirect('admin-view-models')
    
    return render(request, 'delete_subject.html', {"subject_id": subject_id})

# superuser views relating to courses

@login_required
@permission_required('main.can_edit_own_course', raise_exception=True)
def edit_course(request, course_id):
    instance = Course.objects.get(pk=course_id)
    tutor = None

    if request.user.is_superuser:
        pass
    else:
        tutor = Tutor.objects.get(user=request.user)
    
    if tutor is not None:
        if tutor.id is not instance.author.id:
            messages.error(request, "You do not have permission to edit this course")
            return redirect('home')

    if request.method == "POST":
        form = CourseForm(request.POST, instance=instance)

        if form.is_valid():
            form.save()

            title = form.cleaned_data["title"]
            messages.success(request, f"Successfully edited {title} course!")
            if request.user.is_superuser:
                return redirect('admin-view-models')
            else:
                return redirect('tutor-dashboard')
    else:
        form = CourseForm(instance=instance)

    return render(request, "edit_course.html", {"form": form})

@login_required
@permission_required('main.can_delete_own_course', raise_exception=True)
def delete_course(request, course_id, verified=-1):
    instance = Course.objects.get(pk=course_id)
    tutor = None

    if request.user.is_superuser:
        pass
    else:
        tutor = Tutor.objects.get(user=request.user)
    
    if tutor is not None:
        if tutor.id is not instance.author.id:
            messages.error(request, "You do not have permission to delete this course")
            return redirect('home')

    if int(verified) >= 0:
        if int(verified) == 1:
            title = instance.title
            instance.delete()
            messages.success(request, f"Successfully deleted {title} course")
            if request.user.is_superuser:
                return redirect('admin-view-models')
            else:
                return redirect('tutor-dashboard')
        else:
            title = instance.title
            messages.error(request, f"Unable to delete {title} course!")
            if request.user.is_superuser:
                return redirect('admin-view-models')
            else:
                return redirect('tutor-dashboard')
    
    return render(request, 'delete_course.html', {"course_id": course_id})

# superuser views relating to lessons

@login_required
@permission_required('main.can_edit_own_lesson', raise_exception=True)
def edit_lesson(request, lesson_id):
    instance = Lesson.objects.get(pk=lesson_id)
    tutor = None

    if request.user.is_superuser:
        pass
    else:
        tutor = Tutor.objects.get(user=request.user)
    
    if tutor is not None:
        if tutor.id is not instance.author.id:
            messages.error(request, "You do not have permission to edit this lesson")
            return redirect('home')

    if request.method == "POST":
        form = LessonForm(request.POST, instance=instance)

        if form.is_valid():
            form.save()

            title = form.cleaned_data["title"]
            messages.success(request, f"Successfully edited {title} subject!")
            if request.user.is_superuser:
                return redirect('admin-view-models')
            else:
                return redirect('tutor-dashboard')
    else:
        form = LessonForm(instance=instance)

    return render(request, "edit_lesson.html", {"form": form})

@login_required
@permission_required('main.can_delete_own_lesson', raise_exception=True)
def delete_lesson(request, lesson_id, verified=-1):
    instance = Lesson.objects.get(pk=lesson_id)
    tutor = None

    if request.user.is_superuser:
        pass
    else:
        tutor = Tutor.objects.get(user=request.user)
    
    if tutor is not None:
        if tutor.id is not instance.author.id:
            messages.error(request, "You do not have permission to delete this lesson")
            return redirect('home')

    if int(verified) >= 0:
        if int(verified) == 1:
            title = instance.title
            instance.delete()
            messages.success(request, f"Successfully deleted {title} lesson")
            if request.user.is_superuser:
                return redirect('admin-view-models')
            else:
                return redirect('tutor-dashboard')
        else:
            title = instance.title
            messages.error(request, f"Unable to delete {title} lesson!")
            if request.user.is_superuser:
                return redirect('admin-view-models')
            else:
                return redirect('tutor-dashboard')
    
    return render(request, 'delete_lesson.html', {"lesson_id": lesson_id})

# Learner dashboard

def learner_dashboard(request):
    learner = Learner.objects.get(user=request.user)
    courses = learner.courses.all()

    context = {
        "courses": courses,
    }
    return render(request, 'learner_dashboard.html', context)

# Adding/removing courses from learner account

@login_required
@permission_required("main.add_course_to_account")
def add_course_to_learner_account(request, course_id: int):
    if request.user.is_superuser:
        messages.error(request, "Cannot add course to admin account")
        return redirect('admin-view-models')

    learner = Learner.objects.get(user=request.user)
    course = Course.objects.get(pk=course_id)
    
    learner.courses.add(course)
    learner.save()
    messages.success(request, "Successfuly added course to account")
    return redirect('home')

@login_required
@permission_required("main.remove_course_from_account")
def remove_course_from_learner_account(request, course_id: int):
    if request.user.is_superuser:
        messages.error(request, "Cannot remove course from admin account")
        return redirect('admin-view-models')

    learner = Learner.objects.get(user=request.user)
    course = Course.objects.get(pk=course_id)

    learner.courses.remove(course)
    learner.save()
    messages.success(request, "Successfuly added course to account")
    return redirect('home')