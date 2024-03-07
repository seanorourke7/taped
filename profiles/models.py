from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

choices = [
    ('Kildare', 'Kildare'),
    ('Dublin', 'Dublin'),
    ('Laois', 'Laois'),
    ('Carlow', 'Carlow'),
    ('Roscomman', 'Roscomman'),
    ('Kilkenny','Kilkenny'),
    ('Kerry','Kerry'),
    ('Galway','Galway'),
    ('Leitrim','Leitrim'),
    ('Wexford','Wexford'),
    ('Wicklow','Wicklow'),
    ('Waterford','Waterford'),
    ('Cork','Cork'),
    ('Sligo','Sligo'),
    ('Mayo','Mayo'),
    ('Limerick','Limerick'),
    ('Offaly','Offaly'),
    ('Meath','Meath'),
    ('Westmeath','Westmeath'),
    ('Donegal','Donegal'),
    ('Clare','Clare'),
    ('Louth','Louth'),
    ('Monaghan','Monaghan'),
    ('Tipperary','Tipperary'),
    ('Cavan','Cavan'),
    ('Longford','Longford')

    ]


class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_name = models.CharField(max_length=50, null=True, blank=True)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_eircode = models.CharField(max_length=20, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_county = models.CharField(max_length=200, choices=choices, default='Dublin')
    default_country = models.CharField(max_length=2,null=False, blank=True, default='IE')

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()