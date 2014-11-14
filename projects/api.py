# -*- coding: utf-8 -*-

from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from projects.models import Project, Role
from projects.serializers import ProjectSerializer, RoleSerializer


class ProjectsViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (permissions.IsAuthenticated,)


class RolesViewSet(ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = (permissions.IsAuthenticated,)
