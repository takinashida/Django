from django.contrib import admin
from catalog.models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email')
    list_filter = ('email',)
    search_fields = ('email',)