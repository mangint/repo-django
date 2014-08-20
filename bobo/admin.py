from django.contrib import admin
from bobo.models import School, Student
# Register your models here.



class StudentInline(admin.TabularInline):
    model = Student
    extra = 3


class SchoolAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        (None,               {'fields': ['country']}),
    ]
#    search_fields = ['name']
#    inlines = [StudentlInline]
#    list_display = ('first_name', 'last_name')
   

admin.site.register(School, SchoolAdmin)
