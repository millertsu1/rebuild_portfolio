from django.contrib import admin
from .models import Projects,Tag

class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('title', 'description')
    list_filter = ('created_at',)
    filter_horizontal = ('tags',)

class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'color')
    search_fields = ('name',)


admin.site.register(Projects, ProjectAdmin)
admin.site.register(Tag)
