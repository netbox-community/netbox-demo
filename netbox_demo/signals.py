from django.contrib.auth.models import User
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver


@receiver((pre_delete, pre_save), sender=User)
def prevent_admin_user_change(instance, raw=False, **kwargs):
    """
    Prevent changes to the admin user's username or password by raising an exception.
    """
    if instance.pk == 1:
        raise Exception("Admin user may not be modified.")
