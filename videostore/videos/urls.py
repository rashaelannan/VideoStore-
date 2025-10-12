from django.urls import path
from . import views

urlpatterns = [
    path("", views.video_list, name="video-list"),
    path("add/", views.video_create, name="video-add"),
    path("<int:pk>/", views.video_detail, name="video-detail"),
    path("<int:pk>/edit/", views.video_update, name="video-edit"),
    path("<int:pk>/delete/", views.video_delete, name="video-delete"),
]

