from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from MusicApp.albums.forms import CreateAlbumForm, EditAlbumForm, DeleteAlbumForm, DetailsAlbumForm
from MusicApp.albums.models import Album
from MusicApp.utills import get_user_obj


class CreateAlbumView(CreateView):
    model = Album
    form_class = CreateAlbumForm
    template_name = 'albums/album-add.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.owner = get_user_obj()
        return super().form_valid(form)


class EditAlbumView(UpdateView):
    model = Album
    form_class = EditAlbumForm
    pk_url_kwarg = 'id'
    template_name = 'albums/album-edit.html'
    success_url = reverse_lazy('home')


class DetailsAlbumViews(DetailView):
    model = Album
    form_class = DetailsAlbumForm
    pk_url_kwarg = 'id'
    template_name = 'albums/album-details.html'


class DeleteAlbumViews(DeleteView):
    model = Album
    form_class = DeleteAlbumForm
    pk_url_kwarg = 'id'
    template_name = 'albums/album-delete.html'
    success_url = reverse_lazy('home')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)
