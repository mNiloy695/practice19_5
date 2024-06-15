from django.shortcuts import render
# Create your views here.
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Musician
from .forms import MusicianForm

class AddMusicianView(CreateView):
    model=Musician
    form_class=MusicianForm
    template_name='musician.html'
    success_url=reverse_lazy('home')
class EditMusicianView(UpdateView):
    model=Musician
    form_class=MusicianForm
    template_name='musician.html'
    pk_url_kwarg=id
    success_url=reverse_lazy('home')
