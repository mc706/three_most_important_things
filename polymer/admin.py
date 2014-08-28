from django.contrib import admin


from polymer.models import Day, Task


class TaskInline(admin.TabularInline):
    model = Task


class DayAdmin(admin.ModelAdmin):
    list_display = ('date', 'account')
    inlines = [TaskInline]

admin.site.register(Day, DayAdmin)
