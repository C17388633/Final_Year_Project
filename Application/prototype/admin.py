from django.contrib import admin

# Register your models here.
from .models import UserGroup, UserLinkGroup, Note, Event, UserLinkEvent, List, Task, UserPreferences


admin.site.register(UserGroup)
admin.site.register(UserLinkGroup)
admin.site.register(Note)
admin.site.register(Event)
admin.site.register(UserLinkEvent)
admin.site.register(List)
admin.site.register(Task)
admin.site.register(UserPreferences)