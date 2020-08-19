from django.contrib import admin

# Register your models here.
from .models import Profile, Follow

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    pass