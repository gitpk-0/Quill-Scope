from django.shortcuts import render

def index(request):
    """The home page for Quill Scope"""
    return render(request, 'quill_scope_app/index.html')