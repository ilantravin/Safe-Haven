from django.shortcuts import render, redirect
from .models import forum, Discussion
from .forms import *


def home(request):
    '''the function collect all the database data for forum and display it on a page '''
    forums = forum.objects.all()  # getting all subject -> to send for the template and display them
    count = forums.count()  # counting all subjects to show the count in the template
    discussions = []  # List of comments
    comment = CreateInDiscussion()
    for i in forums:
        discussions.append(i.discussion_set.all())  # adding the comments to each forum

    context = {'forums': forums,  # a dictionary to send all the info to the template
               'count': count,
               'discussions': discussions,
               'comment': comment}
    return render(request, 'forum/home.html', context)


def addInForum(request):
    ''' function to add new subject to talk about in the forum '''
    if request.method == 'POST':
        form = CreateInForum(request.POST)  # the subject form with POST data
        if form.is_valid():  # validation check
            form.save()     # if valid we need to save
            return redirect('forum:home')  # if fill correctly the comment will add we be back in the forum home page

    # request.method == 'GET'
    form = CreateInForum()  # empty subject form
    context = {'form': form}  # a dictionary to send all the info to the template
    return render(request, 'forum/addInForum.html', context)


def addInDiscussion(request):
    ''' function to add new comment to a specific subject '''
    msg = None
    if request.method == 'POST':
        form = CreateInDiscussion(request.POST)  # the comment form with POST data

        if form.is_valid() and form.cleaned_data.get('forum') != None:  # validation check
            form.save()  # if valid we need to save
            return redirect('forum:home')  # if fill correctly the comment will add we be back in the forum home page

        if form.cleaned_data.get('forum') == None:  # o send a proper error msg
            msg = 'יש לבחור נושא תקין עליו תרצה להגיב'

    # request.method == 'GET' or not Valid form
    form = CreateInDiscussion()  # empty comment form
    context = {'form': form, 'msg': msg}  # a dictionary to send all the info to the template
    return render(request, 'forum/addInDiscussion.html', context)  # GET or not valid form render the empty form
