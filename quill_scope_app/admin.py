from django.contrib import admin

# import models to be registered
from .models import Topic

# manage model thru admin site
admin.site.register(Topic)
