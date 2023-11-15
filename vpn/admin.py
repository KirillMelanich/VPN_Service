from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from vpn.models import User, Site, Statistics, InternalRoute


@admin.register(User)
class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("preferences",)
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("preferences",)}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "preferences",
                    )
                },
            ),
        )
    )


admin.site.register(Site)
admin.site.register(Statistics)
admin.site.register(InternalRoute)
