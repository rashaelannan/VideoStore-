from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # we won't use admin in this assignment (but leaving the line is harmless)
    # path('admin/', admin.site.urls),

    path("videos/", include("videos.urls")),
    path("", include("videos.urls")),  # optional: make list view the homepage
]

