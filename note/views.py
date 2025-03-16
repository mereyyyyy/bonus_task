from django.shortcuts import render, get_object_or_404, redirect
from .models import Note

def note_list(request):
    notes = Note.objects.all()
    return render(request, 'note/note_list.html', {'notes': notes})

def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'note/note_detail.html', {'note': note})

def note_create(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        Note.objects.create(title=title, content=content)
        return redirect('note_list')
    return render(request, 'note/note_form.html')

def note_update(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        note.title = request.POST['title']
        note.content = request.POST['content']
        note.save()
        return redirect('note_list')
    return render(request, 'note/note_form.html', {'note': note})

def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        note.delete()
        return redirect('note_list')
    return render(request, 'note/note_confirm_delete.html', {'note': note})
