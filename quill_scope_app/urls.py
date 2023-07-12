"""Defines URL patterns for quill_scope_app."""

from django.urls import path

from . import views

app_name = 'quill_scope_app'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # All topics page
    path('topics/', views.topics, name='topics'),

    # Detail page for a given topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    # Page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic'),

    # Page for adding a new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),

    # Page for editing an entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),

    # # Page for deleting an entry
    # path('delete_entry/<int:entry_id>/', views.delete_entry, name='delete_entry'),

    # # Page for editing a topic
    # path('edit_topic/<int:topic_id>/', views.edit_topic, name='edit_topic'),

    # # Page for deleting a topic
    # path('delete_topic/<int:topic_id>/', views.delete_topic, name='delete_topic'),


]