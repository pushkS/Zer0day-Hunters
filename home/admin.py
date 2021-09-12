from django.contrib import admin
from home.models import Contact
from home.models import Index, Career, About, Training

# Register your models here.
admin.site.register(Index)
admin.site.register(Contact)
admin.site.register(About)
admin.site.register(Career)
admin.site.register(Training)