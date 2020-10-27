from django.contrib import admin

from .models import Profile,Project,countries,Rating




# Register your models here.

admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(countries)
admin.site.register(Rating)

