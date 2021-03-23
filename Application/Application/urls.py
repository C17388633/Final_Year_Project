"""Application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView
from prototype.views import *


# For rest framework
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework import permissions
from rest_framework.schemas import get_schema_view


# User
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


# Note
class NoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Note
        fields = ['user', 'note_title', 'note_content']


# ViewSets define the view behavior.
class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'notes', NoteViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('prototype/', include('prototype.urls')),
    path('prototype/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('settings/', TemplateView.as_view(template_name='settings.html'), name='settings'),
    # Schedule
    path('schedule/', events_view, name='schedule'),
    path('schedule/createEvent/', create_event_view, name='AddEvent'),
    path('schedule/<int:id>/editEvent/', edit_event_view, name='EditEvent'),
    path('schedule/<int:id>/deleteEvent/', delete_event_view, name='DeleteEvent'),
    path('schedule/search/', search_event_view, name='SearchEvent'),
    # To do list
    path('to-do-list/', lists_view, name='tasks'),
    path('to-do-list/createList/', create_list_view, name='AddList'),
    path('to-do-list/<int:id>/editList/', edit_list_view, name='EditList'),
    path('to-do-list/<int:id>/deleteList/', delete_list_view, name='DeleteList'),
    path('to-do-list/searchList/', search_list_view, name='SearchList'),
    # Task
    path('to-do-list/createTask/', create_task_view, name='AddTask'),
    path('to-do-list/<int:id>/editTask/', edit_task_view, name='EditTask'),
    path('to-do-list/<int:id>/completedTask/', complete_task_view, name='CompleteTask'),
    path('to-do-list/viewCompletedTasks/', completed_tasks_view, name='CompletedTasks'),
    path('to-do-list/<int:id>/incompleteTask/', incomplete_task_view, name='IncompleteTask'),
    path('to-do-list/<int:id>/deleteTask/', delete_task_view, name='DeleteTask'),
    path('to-do-list/searchTask/', search_task_view, name='SearchTask'),
    # path('tasks/', TemplateView.as_view(template_name='tasks.html'), name='tasks'),
    # Notes
    path('notes/', notes_page, name='notes'),
    path('notes/createNote/', create_note_view, name='AddNote'),
    path('notes/<int:id>/editNote/', edit_note_view, name='EditNote'),
    path('notes/<int:id>/deleteNote/', delete_note_view, name='DeleteNote'),
    path('notes/search/', search_note_view, name='SearchNote'),
    # path('notes/', TemplateView.as_view(template_name='notes.html'), name='notes'),
    # Rest Api stuff
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('openapi', get_schema_view(
            title="Planneroid",
            description="Scheduling, to do lists and a notes keeping application",
            version="1.0.0"
        ), name='openapi-schema'),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger_ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),

]
