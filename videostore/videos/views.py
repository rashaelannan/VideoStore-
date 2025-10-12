from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Video
from .forms import VideoForm

# READ (list)
def video_list(request):
    videos = Video.objects.order_by("MovieTitle")
    return render(request, "videos/video_list.html", {"videos": videos})

# READ (detail)
def video_detail(request, pk):
    video = get_object_or_404(Video, pk=pk)
    return render(request, "videos/video_detail.html", {"video": video})

# CREATE
def video_create(request):
    if request.method == "POST":
        form = VideoForm(request.POST)
        if form.is_valid():
            form.save()  # MovieID auto generated
            return redirect("video-list")
    else:
        form = VideoForm()
    return render(request, "videos/video_form.html", {"form": form, "mode": "Create"})

# UPDATE
def video_update(request, pk):
    video = get_object_or_404(Video, pk=pk)
    if request.method == "POST":
        form = VideoForm(request.POST, instance=video)
        if form.is_valid():
            form.save()
            return redirect("video-detail", pk=video.pk)
    else:
        form = VideoForm(instance=video)
    return render(request, "videos/video_form.html", {"form": form, "mode": "Update", "video": video})

# DELETE
def video_delete(request, pk):
    video = get_object_or_404(Video, pk=pk)
    if request.method == "POST":
        video.delete()
        return redirect("video-list")
    return render(request, "videos/video_confirm_delete.html", {"video": video})

