from django.contrib import admin
from .models import *

admin.site.register(MyUser)
admin.site.register(Song)
admin.site.register(Option)

admin.site.register(
    Room,
    list_display=["id", "title", "staff_only"],
    list_display_links=["id", "title"],
)
