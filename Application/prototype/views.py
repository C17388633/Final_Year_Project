from django.shortcuts import render, get_object_or_404, redirect
# for forms
from .forms import *


# For Signup page
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .models import Note, List, Task, Event
# For searching


# Create your views here.
# Signup page
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


# Schedule
# Event page
def events_view(request, *args, **kwargs):
    print(request.headers)
    queryset = Event.objects.filter(user=request.user).order_by('start_date')
    context = {
        "event_list": queryset,
    }
    return render(request, 'schedule/schedule.html', context)


# Event Form
def create_event_view(request):
    creator = Event(user=request.user)
    form = EventForm(request.POST, instance=creator)
    if form.is_valid():
        creator.save()
        return redirect('../')

    return render(request, 'schedule/add_event.html', {'form': form})


# Edit Event
def edit_event_view(request, id):
    obj = get_object_or_404(Event, event_id=id)
    form = EventForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('../../')
    context = {
        'form': form
    }
    return render(request, "schedule/edit_event.html", context)


# Delete Event
def delete_event_view(request, id):
    event = get_object_or_404(Event, event_id=id)
    if request.method == "POST":
        event.delete()
        return redirect('../../')
    context = {
        "event": event
    }
    return render(request, "schedule/delete_event.html", context)


# Search Event
def search_event_view(request):
    event_query = request.GET.get('event_query')
    queryset = Event.objects.filter(user=request.user, event_title__icontains=event_query)
    context = {
        "event_list": queryset
    }
    return render(request, 'schedule/search_event_results.html', context)


# To do Lists
# To do list page
def lists_view(request, *args, **kwargs):
    print(request.headers)
    queryset = List.objects.filter(user=request.user)
    queryset2 = Task.objects.filter(user=request.user, complete__icontains=0).order_by('task_datetime')
    context = {
        "lists": queryset,
        "tasks": queryset2
    }
    return render(request, 'to-do-lists/to-do-lists.html', context)


# List Form
def create_list_view(request):
    creator = List(user=request.user)
    form = ListForm(request.POST, instance=creator)
    if form.is_valid():
        creator.save()
        return redirect('../')

    return render(request, 'to-do-lists/add_list.html', {'form': form})


# Edit list
def edit_list_view(request, id):
    obj = get_object_or_404(List, list_id=id)
    form = ListForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('../../')
    context = {
        'form': form
    }
    return render(request, "to-do-lists/edit_list.html", context)


# Delete list
def delete_list_view(request, id):
    list = get_object_or_404(List, list_id=id)
    if request.method == "POST":
        list.delete()
        return redirect('../../')
    context = {
        "list": list
    }
    return render(request, "to-do-lists/delete_list.html", context)


# Search List
def search_list_view(request):
    list_query = request.GET.get('list_query')
    queryset = List.objects.filter(user=request.user, list_title__icontains=list_query)
    queryset2 = Task.objects.filter(user=request.user)
    context = {
        "lists": queryset,
        "tasks": queryset2
    }
    return render(request, 'to-do-lists/search_lists_results.html', context)


# Task Form
def create_task_view(request):
    user = request.user
    creator = Task(user=request.user)
    form = TaskForm(user, request.POST, instance=creator)
    if form.is_valid():
        form.save()
        return redirect('../')
    return render(request, 'to-do-lists/add_task.html', {'form': form})


# Edit Task
def edit_task_view(request, id):
    obj = get_object_or_404(Task, task_id=id)
    form = EditTaskForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('../../')
    context = {
        'form': form
    }
    return render(request, "to-do-lists/edit_task.html", context)


# Complete Task
def complete_task_view(request, id):
    task = Task.objects.get(task_id=id)
    task.complete = 1
    task.save()

    return redirect('tasks')


# view lists
def completed_tasks_view(request, *args, **kwargs):
    print(request.headers)
    queryset = List.objects.filter(user=request.user)
    queryset2 = Task.objects.filter(user=request.user, complete__icontains=1).order_by('task_datetime')
    context = {
        "lists": queryset,
        "tasks": queryset2
    }
    return render(request, 'to-do-lists/completed_tasks.html', context)


# Incomplete Task
def incomplete_task_view(request, id):
    task = Task.objects.get(task_id=id)
    task.complete = 0
    task.save()

    return redirect('tasks')


# Delete Task
def delete_task_view(request, id):
    task = get_object_or_404(Task, task_id=id)
    if request.method == "POST":
        task.delete()
        return redirect('../../')
    context = {
        "task": task
    }
    return render(request, "to-do-lists/delete_task.html", context)


# Search Task
def search_task_view(request):
    task_query = request.GET.get('task_query')
    queryset = Task.objects.filter(user=request.user, task_title__icontains=task_query)
    queryset2 = List.objects.filter(user=request.user)
    context = {
        "tasks": queryset,
        "lists": queryset2
    }
    return render(request, 'to-do-lists/search_tasks_results.html', context)


# Notes
# Notes page
def notes_page(request, *args, **kwargs):
    print(request.headers)
    queryset = Note.objects.filter(user=request.user)
    context = {
        "note_list": queryset
    }
    return render(request, 'notes/notes.html', context)


# Note form
def create_note_view(request):
    creator = Note(user=request.user)
    form = NoteForm(request.POST, instance=creator)
    if form.is_valid():
        creator.save()
        return redirect('../')

    return render(request, 'notes/add_note.html', {'form': form})


# Edit Note
def edit_note_view(request, id):
    obj = get_object_or_404(Note, note_id=id)
    form = NoteForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('../../')
    context = {
        'form': form
    }
    return render(request, "notes/edit_note.html", context)


# Delete note
def delete_note_view(request, id):
    note = get_object_or_404(Note, note_id=id)
    if request.method == "POST":
        note.delete()
        return redirect('../../')
    context = {
        "note": note
    }
    return render(request, "notes/delete_note.html", context)


# Search Note
def search_note_view(request):
    note_query = request.GET.get('note_query')
    queryset = Note.objects.filter(user=request.user, note_title__icontains=note_query)
    context = {
        "note_list": queryset
    }
    return render(request, 'notes/search_notes_results.html', context)



# class search_note_view(ListView):
#    model = Note
#    template_name = 'notes/search_notes_results.html'

#    def get_queryset(self):
#        query = self.request.GET.get('note_query')
#        user = self.request.GET.get('user')
#        note_list = Note.objects.filter(
#            Q(note_title__icontains=query) | Q(note_content__icontains=query)
#        )
#        return note_list
