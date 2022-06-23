from django.contrib import admin

from .models import Items
admin.site.register(Items)

from .models import Contact
admin.site.register(Contact)