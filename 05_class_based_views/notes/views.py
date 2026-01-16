from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Note

class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    # template_name = 'notes/note_list.html' (default)
    # context_object_name = 'note_list' (default)

    def get_queryset(self):
        # Users can only view their own notes
        return Note.objects.filter(owner=self.request.user)

class NoteDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Note

    def test_func(self):
        # Authorization: Note owner must be the current user
        note = self.get_object()
        return self.request.user == note.owner

class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    fields = ['title', 'content']
    success_url = reverse_lazy('note-list')

    def form_valid(self, form):
        # Auto-set the owner to the current logged-in user
        form.instance.owner = self.request.user
        return super().form_valid(form)

class NoteUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Note
    fields = ['title', 'content']
    success_url = reverse_lazy('note-list')

    def test_func(self):
        note = self.get_object()
        return self.request.user == note.owner

class NoteDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Note
    success_url = reverse_lazy('note-list')

    def test_func(self):
        note = self.get_object()
        return self.request.user == note.owner
