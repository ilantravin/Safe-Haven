from django.shortcuts import render, redirect
from .forms import storyForm
from .models import story


def create_story(request):
    if request.method == 'POST':
        form = storyForm(request.POST)
        if form.is_valid():
            new_story = form.save()
            new_story.save()
            return redirect('success_story:all_stories')
    return render(request, 'success_story/create_story.html', {'form': storyForm()})


def all_stories(request):
    stories = story.objects.all()
    return render(request, 'success_story/all_stories.html', {'stories': stories})

