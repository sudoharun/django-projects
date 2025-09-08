from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, Permission
from .models import Tutor, Learner

@receiver(post_save, sender=Tutor)
def sync_user_permissions(sender, instance, created, **kwargs):
    if created:
        # When a new Tutor is created, assign the Tutor's permissions to the associated User
        user = instance.user

        # Fetch all permissions for the Tutor model
        permissions = Permission.objects.filter(content_type__model='tutor')

        # Add the permissions to the User
        for permission in permissions:
            user.user_permissions.add(permission)

        # Save the User to persist the permissions
        user.save()

@receiver(post_save, sender=Learner)
def sync_user_permissions(sender, instance, created, **kwargs):
    if created:
        # When a new Tutor is created, assign the Tutor's permissions to the associated User
        user = instance.user

        # Fetch all permissions for the Tutor model
        permissions = Permission.objects.filter(content_type__model='learner')

        # Add the permissions to the User
        for permission in permissions:
            user.user_permissions.add(permission)

        # Save the User to persist the permissions
        user.save()