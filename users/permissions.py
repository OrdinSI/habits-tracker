from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """Class for checking if the user is the owner of the object."""

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class IsAdmin(permissions.BasePermission):
    """Class for checking if the user is admin."""

    def has_permission(self, request, view):
        return request.user.is_superuser
