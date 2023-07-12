from django.shortcuts import render

from .models import Topic

def index(request):
    """The home page for Quill Scope"""
    return render(request, 'quill_scope_app/index.html')

def topics(request):
    """Show all topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return render(request, 'quill_scope_app/topics.html', context)