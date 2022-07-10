from django.contrib import admin
from .models import Student, Marksheet

# Register your models here.

class MarksheetInline(admin.TabularInline):
    model = Marksheet
    extra: int = 3

class StudentAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['name', 'grade', 'dob']})]
    inlines = [MarksheetInline]

admin.site.register(Student, StudentAdmin)
