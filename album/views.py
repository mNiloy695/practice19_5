
from django.views.generic import CreateView,UpdateView,DeleteView
from .models import Album
from .forms import AlbumForm
from django.urls import reverse_lazy

class AddAlbumView(CreateView):
    model=Album 
    form_class=AlbumForm
    template_name='album.html'
    success_url=reverse_lazy('home')
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['type']='Update Your Profile'
        return context
class UpdateAlbumView(UpdateView):
    model=Album
    form_class=AlbumForm
    template_name='album.html'
    pk_url_kwarg=id
    success_url=reverse_lazy('home')
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['type']='Update Your Profile'
        return context
class DeleteAlbumView(DeleteView):
    model=Album
    template_name='delete.html'
    pk_url_kwarg=id
    success_url=reverse_lazy('home')