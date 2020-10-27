from django.contrib import admin

from .models import Countries,Profile,Project,Rating




# Register your models here.

admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Countries)
admin.site.register(Rating)

