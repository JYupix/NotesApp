from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from .models import Note
from .serializers import NoteSerializer
from .forms import NoteForm
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages

class NotesView(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

def notes_list(request):
    q = request.GET.get('q', '')
    archived_count = Note.objects.filter(is_archived=True).count()
    notes = Note.objects.filter(is_archived=False)

    if q:
        notes = Note.objects.filter(Q(title__icontains=q) | Q(content__icontains=q))

    paginator = Paginator(notes, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'notes.html', {'notes': page_obj, 'q': q, 'archived_count':archived_count})

def notes_archived(request):
    q = request.GET.get('q', '')
    notes = Note.objects.filter(is_archived=True)  

    if q:
        notes = Note.objects.filter(Q(title__icontains=q) | Q(content__icontains=q))
    
    paginator = Paginator(notes, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'archived_notes.html', {'notes': page_obj, 'q':q})

def note_archived(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if note.is_archived == False:
        note.is_archived = True
        note.save()
        messages.success(request, ("Note Archived!"))
    elif note.is_archived == True:
        note.is_archived = False
        note.save()
        messages.success(request, ("Note Unarchived!"))
    return redirect('notes_list')


def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            messages.success(request, ("Note Created!"))
            return redirect('notes_list')
    else:
        form = NoteForm()
    return render(request, 'note_create.html', {'form': form})

def note_update(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            messages.success(request, ("Note Updated!"))
            return redirect('notes_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'note_uptate.html', {'form':form, 'note':note})

def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    messages.success(request, ("Note Deleted!"))
    return redirect('notes_list')