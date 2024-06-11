from django.contrib import admin
from userauth.models import User, Profile

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    search_fields = ['fullname', 'username']
    list_display = ['username',  'email',  ]


class ProfileAdmin(admin.ModelAdmin):
    search_fields = ['fullname', 'user__username', 'image_tag']
    list_display = ['fullname', 'user', 'gender', 'image_tag']
    # readonly_fields = ['image_tag']



admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)