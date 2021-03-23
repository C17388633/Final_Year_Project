from django import forms
from django.forms import DateTimeInput

from .models import Note, List, Task, Event


# Create a note
class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        exclude = ('user',)
        fields = [
            'note_title',
            'note_content'
        ]


# Create a List
class ListForm(forms.ModelForm):
    class Meta:
        model = List
        exclude = ('user',)
        fields = [
            'list_title'
        ]


# Create a Task
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ('user',)
        fields = [
            'task_title',
            'task_description',
            'task_datetime',
            'task_list',
            'colour'
        ]

        widgets = {
            'task_datetime': DateTimeInput(attrs={'type': 'date'}),
        }

    def __init__(self, user, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['task_list'].queryset = List.objects.filter(user=user)


class EditTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ('user', 'task_list')
        fields = [
            'task_title',
            'task_description',
            'task_datetime',
            'colour'
        ]

        widgets = {
            'task_datetime': DateTimeInput(attrs={'type': 'date'}),
        }


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ('user',)
        fields = [
            'event_title',
            'event_description',
            'location',
            'start_date',
            'end_date',
            'colour'
        ]

        widgets = {
            'start_date': DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_date': DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def clean_end_date(self):
        start_date = self.cleaned_data.get("end_date")
        end_date = self.cleaned_data.get("end_date")
        if end_date < start_date:
            raise forms.ValidationError("End date should be greater than start date.")
        return end_date
