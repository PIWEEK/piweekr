# -*- coding: utf-8 -*-

from rest_framework import serializers

from projects.models import Project, Role, ProjectRole


class ProjectRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectRole


class ProjectSerializer(serializers.ModelSerializer):
    project_roles = ProjectRoleSerializer(read_only=True)

    class Meta:
        model = Project


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
