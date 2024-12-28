from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content',]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 mt-1 rounded-md bg-gray-700 text-white focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter the task title'
            }),
            'content': forms.Textarea(attrs={
                'class': 'w-full px-4 py-2 mt-1 rounded-md bg-gray-700 text-white focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter the task content',
                'rows': 4
            }),
        }