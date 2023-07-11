from django.contrib import admin

# import models to be registered
from .models import Topic, Entry

# manage models thru admin site
admin.site.register(Topic)
admin.site.register(Entry)
