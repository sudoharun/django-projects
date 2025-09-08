from django.shortcuts import render, redirect
from django.apps import apps
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User
from .models import User, Recipe, Cake
from .forms import CustomUserCreationForm, CustomUserChangeForm, RecipeForm, CakeForm

# Create your views here.
def homepage(request):
    context = {
        'recipes': Recipe.objects.all(),
        'cakes': Cake.objects.all(),
    }
    return render(request, 'homepage.html', context)

def moreDetails(request, app_name, parent_model, model_id):
    p_model = apps.get_model(app_name, parent_model)
    model = p_model.objects.get(pk=model_id)
    context = {
        'model_name': parent_model,
        'model': model,
    }
    return render(request, 'details.html', context)

def logIn(request, username=None, password=None):
    if request.user.is_authenticated:
        messages.error(request, 'Already logged in!')
        return redirect('homepage')

    if (username and password) is not None:
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully been logged in!')
            return redirect('homepage')
        else:
            messages.error(request, 'There was an error logging you in!')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in!')
            return redirect('homepage')
        else:
            messages.error(request, 'There was an error logging you in!')

    return render(request, 'login.html', {})

def logOut(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'Successfully logged out!')
        return redirect('homepage')
    else:
        messages.error(request, 'Unable able to sign out if you aren\'t logged in!')
        return redirect('homepage')

def signUp(request):
    if request.user.is_authenticated:
        messages.error(request, 'Already logged in!')
        return redirect('homepage')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Successfully Created!')
            return redirect('homepage')
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form,
    }
    return render(request, 'signup.html', context)

def dashboard(request):
    if not request.user.is_authenticated:
        messages.error(request, 'There was an error viewing your account! (You are not logged in)')
        return redirect('homepage')

    context = {}

    if request.user.is_superuser:
        context['users'] = User.objects.all()
        context['recipes'] = Recipe.objects.all()
        context['cakes'] = Cake.objects.all()
        context['username'] = request.user.username
        return render(request, 'admin_dashboard.html', context)
    else:
        return render(request, 'regular_dashboard.html', context)

def changePassword(request, user_id):
    context = {}
    return render(request, 'change_password.html', context)

def editModel(request, parent_model, model_id):
    p_model = apps.get_model('mainapp', parent_model)
    model = p_model.objects.get(pk=model_id)

    if request.method == "POST":
        if parent_model == "User":
            form = CustomUserChangeForm(request.POST, instance=model)
        elif parent_model == "Recipe":
            form = RecipeForm(request.POST, instance=model)
        elif parent_model == "Cake":
            form = CakeForm(request.POST, instance=model)
        else:
            messages.error(request, 'There was an error!')
            return redirect("dashboard")
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        if parent_model == "User":
            form = CustomUserChangeForm(instance=model)
        elif parent_model == "Recipe":
            form = RecipeForm(instance=model)
        elif parent_model == "Cake":
            form = CakeForm(instance=model)
        else:
            messages.error(request, 'An error has occurred!')
            return redirect('dashboard')

    context = {
        'parent_model': parent_model,
        'model_id': model_id,
        'form': form,
    }
    return render(request, 'edit_model.html', context)

def createModel(request, model_name):
    if model_name == 'User':
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
        else:
            form = CustomUserCreationForm()
    elif model_name == 'Recipe':
        if request.method == 'POST':
            form = RecipeForm(request.POST)
        else:
            form = RecipeForm()
    elif model_name == 'Cake':
        if request.method == 'POST':
            form = CakeForm(request.POST)
        else:
            form = CakeForm()
    else:
        messages.error(request, 'An error has occurred!')
        return redirect('dashboard')

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully created model!')
            return redirect('dashboard')

    context = {
        'model_name': model_name,
        'form': form,
    }
    return render(request, 'create_model.html', context)

def deleteModel(request, parent_model, model_id):
    model = apps.get_model('mainapp', parent_model)
    model.objects.get(pk=model_id).delete()
    return redirect("dashboard")
