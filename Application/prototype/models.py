from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import date



# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return f"{self.user}"

    #
    # Signal
    #
    @receiver(post_save, sender=get_user_model())
    def manage_user_profile(sender, instance, created, **kwargs):
        try:
            my_profile = instance.profile
            my_profile.save()
        except Profile.DoesNotExist:
            Profile.objects.create(user=instance)


# User Group model
class UserGroup(models.Model):
    group_id = models.AutoField(primary_key=True)
    group_title = models.CharField(max_length=50, null=False)
    group_code = models.CharField(max_length=50, null=False)


# User Link Group model
class UserLinkGroup(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    group = models.ForeignKey(UserGroup, on_delete=models.CASCADE)


# Note Table
class Note(models.Model):
    note_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    note_title = models.CharField(max_length=50)
    note_content = models.CharField(max_length=300)

    def __str__(self):
        return self.note_title


# Event model
class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_title = models.CharField(max_length=50, null=False)
    event_description = models.CharField(max_length=300)
    location = models.CharField(max_length=200)
    # date for events (YYYY,MM,DD,HH,mm,ss)
    start_date = models.DateTimeField(editable=True, null=False)
    end_date = models.DateTimeField(editable=True, null=False)
    # Colour of event
    # Colour Choices
    Colour_CHOICES = [
        ('White (default)', 'white'), ('Red', 'red'), ('Blue', 'blue'), ('Yellow', 'yellow'), ('Green', 'green'),
        ('Purple', 'purple'), ('Orange', 'orange'), ('Pink', 'pink'),
    ]
    colour = models.CharField(max_length=15, choices=Colour_CHOICES, )
    # User Foreign key.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # group = models.ForeignKey(UserGroup, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.event_title


# User Link Event model
class UserLinkEvent(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)


# List model
class List(models.Model):
    list_id = models.AutoField(primary_key=True)
    list_title = models.CharField(max_length=50, null=False)
    # User
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.list_title


# Task model
class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    task_title = models.CharField(max_length=50, null=False)
    task_description = models.CharField(max_length=300)
    task_datetime = models.DateField(editable=True, null=False)
    complete = models.IntegerField(editable=True, default=0)
    # Colour Choices
    Colour_CHOICES = [
        ('White (default)', 'white'), ('Red', 'red'), ('Blue', 'blue'), ('Yellow', 'yellow'), ('Green', 'green'),
        ('Purple', 'purple'), ('Orange', 'orange'), ('Pink', 'pink'),
    ]
    colour = models.CharField(max_length=15, choices=Colour_CHOICES, default="White (default)")
    # Foreign keys
    task_list = models.ForeignKey(List, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.task_title





# User Preferences model
class UserPreferences(models.Model):
    Theme = models.IntegerField(default=1)
    font_size = models.IntegerField(default=15)
    colourblind = models.IntegerField(default=0)
    # notifications needed here
