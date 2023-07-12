"""Defines URL patterns for quill_scope_app."""

from django.urls import path

from . import views

app_name = 'quill_scope_app'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # All topics page
    path('topics/', views.topics, name='topics'),
]