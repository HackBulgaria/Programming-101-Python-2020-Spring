from django.contrib import admin

from education.models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_duration', 'start_date', 'end_date')

    def get_duration(self, obj):
        if obj.duration:
            return f'{obj.duration.days // 7} weeks'

        return 'N/A'

    get_duration.short_description = 'Duration'
