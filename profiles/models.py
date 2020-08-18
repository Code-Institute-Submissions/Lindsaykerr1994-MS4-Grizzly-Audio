from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    # Handle any user's information
    # Copied from checkout.models
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20, null=False,
                                            blank=False, default=" ")
    default_street_address1 = models.CharField(max_length=80, null=False,
                                               blank=False, default=" ")
    default_street_address2 = models.CharField(max_length=80, null=False,
                                               blank=False, default=" ")
    default_town_or_city = models.CharField(max_length=40, null=False,
                                            blank=False, default=" ")
    default_county = models.CharField(max_length=40, null=False,
                                      blank=False, default=" ")
    default_post_code = models.CharField(max_length=10, null=False,
                                         blank=False, default=" ")
    default_country = CountryField(blank_label='Country', null=True,
                                   blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    # Handles a user profile creating or update
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()
