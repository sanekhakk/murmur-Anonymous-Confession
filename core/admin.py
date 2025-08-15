
# Register your models here.
from django.contrib import admin
from .models import Confession

@admin.register(Confession)
class ConfessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_message', 'upvotes', 'is_trending', 'created_at')
    list_editable = ('upvotes', 'is_trending')
    search_fields = ('message',)
    list_filter = ('is_trending', 'created_at')

    def short_message(self, obj):
        return obj.message[:50] + "..." if len(obj.message) > 50 else obj.message
    short_message.short_description = 'Message'