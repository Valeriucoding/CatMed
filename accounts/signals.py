from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

User = get_user_model()

@receiver(pre_save, sender=User)
def update_username_from_email(sender, instance, **kwargs):
    if instance.email:
        base_username = slugify(instance.email.split('@')[0])[:150]  # Use 150 chars max
        username = base_username
        n = 1

        while User.objects.exclude(pk=instance.pk).filter(username=username).exists():
            n += 1
            username = f"{base_username[:145]}-{n}"  # Keep it within 150 chars

        instance.username = username
