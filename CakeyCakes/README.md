# Usage instructions:

1. Make sure you have nodejs/npm installed
2. Required packages:
    - django
    - django-tailwind
    - django-tailwind[reload]
    - django-multiselectfield
    - django-crispy-forms
    - crispy-tailwind
3. Go into project directory
4. If on Windows (CakeyCakes/settings.py):
    - Uncomment line 137 and comment out line 136
    - Comment out line 46 and uncomment line 45
5. Do `python manage.py tailwind init` then quit (Ctrl+C) when it asks for a name for the theme app
6. Do `python manage.py tailwind install`. If you get an error on Windows, uncomment line 139 in CakeyCakes/settings.py and edit as required
7. On a separate terminal, do `python manage.py tailwind start`
8. On a separate terminal, do `python manage.py runserver`

# Administrator account:

Username: admin

Password: admin
