from django.contrib import admin

from projects.models import Project, Role, ProjectRole

class ProjectRoleInline(admin.TabularInline):
    model = ProjectRole

class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        ProjectRoleInline,
    ]

admin.site.register(Project, ProjectAdmin)

class RoleAdmin(admin.ModelAdmin):
    pass
admin.site.register(Role, RoleAdmin)
