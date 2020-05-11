from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ('fullName', 'email', 'matric_no')
    list_per_page = 10
    search_fields = ('id',)

    class Meta:
        model = Student


admin.site.register(Student, StudentAdmin)
