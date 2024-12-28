from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'notes', views.NotesView, 'notes')

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.notes_list, name='notes_list'),
    path('create/', views.note_create, name='note-create'),
    path('update/<int:pk>/', views.note_update, name='note-update'),
    path('delete/<int:pk>/', views.note_delete, name='note-delete'),
    path('archived/', views.notes_archived, name='notes-archived'),
    path('archived/<int:pk>', views.note_archived, name='note-archived'),
]