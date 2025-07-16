from django import forms
from events.models import Category, Event, Participant


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'event_date', 'event_time', 'location', 'category']

class EventUpdateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'event_date', 'event_time', 'location', 'category']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full bg-transparent text-slate-700 text-sm border border-slate-200 rounded-md pl-3 py-2'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full bg-transparent text-slate-700 text-sm border border-slate-200 rounded-md pl-3 py-2 resize-none',
                'rows': 4
            }),
            'event_date': forms.TextInput(attrs={
                'class': 'w-full bg-transparent text-slate-700 text-sm border border-slate-200 rounded-md pl-3 py-2',
                'placeholder': 'YYYY-MM-DD'
            }),
            'event_time': forms.TimeInput(attrs={
                'class': 'w-full bg-transparent text-slate-700 text-sm border border-slate-200 rounded-md pl-3 py-2',
                'type': 'time'
            }),
            'location': forms.TextInput(attrs={
                'class': 'w-full bg-transparent text-slate-700 text-sm border border-slate-200 rounded-md pl-3 py-2'
            }),
            'category': forms.RadioSelect(attrs={
                'class': 'form-radio text-md ml-2'
            })
        }

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['name', 'email', 'total_events']

class ParticipantUpdateForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['name', 'email', 'total_events']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full bg-transparent text-slate-700 text-sm border border-slate-200 rounded-md pl-3 py-2'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full bg-transparent text-slate-700 text-sm border border-slate-200 rounded-md pl-3 py-2'
            }),
            'total_events': forms.CheckboxSelectMultiple(attrs={
                'class': 'text-lg'
            })
        }

class CategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full bg-transparent text-slate-700 text-sm border border-slate-200 rounded-md pl-3 py-2'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full bg-transparent text-slate-700 text-sm border border-slate-200 rounded-md pl-3 py-2 resize-none',
                'rows': 4
            }),
        }