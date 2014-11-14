from rest_framework.routers import DefaultRouter, SimpleRouter
from projects.api import ProjectsViewSet, RolesViewSet

router = DefaultRouter()
router.register("projects", ProjectsViewSet, base_name="projects")
router.register("roles", RolesViewSet, base_name="roles")
