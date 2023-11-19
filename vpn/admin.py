from django.contrib import admin

from vpn.models import User, Site, Statistics, InternalRoute, Profile

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Site)
admin.site.register(Statistics)
admin.site.register(InternalRoute)
