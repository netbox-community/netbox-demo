from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver


@receiver(pre_save, sender=User)
def prevent_admin_user_change(instance, raw=False, **kwargs):
    """
    Prevent changes to the admin user's username, password, or active status.
    """
    if instance.pk == 1:
        if instance.username != settings.PLUGINS_CONFIG['netbox_demo']['admin_username']:
            raise Exception("Admin user may not be renamed.")
        if instance._password:
            raise Exception("Admin user password may not be changed.")
        if not instance.is_active:
            raise Exception("Admin user may not be disabled.")


@receiver(pre_delete, sender=User)
def prevent_admin_user_deletion(instance, raw=False, **kwargs):
    """
    Prevent deletion of the admin user.
    """
    if instance.pk == 1:
        raise Exception("Admin user may not be deleted.")
