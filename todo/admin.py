from django.contrib import admin
from .models import Todo
from django.utils import timezone
from pytz import timezone as pytz_timezone


class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'display_created',)

    def display_created(self, obj):
        tz = pytz_timezone('Asia/Yerevan')  # Change 'Asia/Yerevan' to your desired timezone
        local_time = timezone.localtime(obj.created, timezone=tz)
        return local_time.strftime('%Y-%m-%d %H:%M:%S')

    display_created.short_description = 'Created (Yerevan Time)'  # Change the display name if desired

admin.site.register(Todo, TodoAdmin)


# class TodoAdmin2(admin.ModelAdmin):
#     readonly_fields2 = ('created',)
#
# admin.site.register(Todo,TodoAdmin2)


