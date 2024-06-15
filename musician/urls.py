from django.urls import path
from . import views

urlpatterns=[
  path('edit_musician/<int:id>',views.EditMusicianView.as_view(),name='edit_musician'),
  path('add_musician',views.AddMusicianView.as_view(),name='add_musician'),
]