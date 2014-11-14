from django.db import models

class Role(models.Model):
    name = models.CharField(null=False, blank=False, max_length=30)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(null=False, blank=False, max_length=100)
    description = models.TextField(null=True, blank=True)
    roles = models.ManyToManyField(Role, through="projects.ProjectRole", related_name="roles")
    creator = models.ForeignKey("auth.User", related_name="projects")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ProjectRole(models.Model):
    project = models.ForeignKey(Project, null=False, blank=False, related_name="project_roles")
    role = models.ForeignKey(Role, null=False, blank=False, related_name="role_projects")
    quantity = models.FloatField()

    def __str__(self):
        return "{} - {}".format(self.project.name, self.role.name)
