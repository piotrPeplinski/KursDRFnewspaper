from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow owners of an object to edit and delete it,
    but read-only access to others.
    """

    def has_object_permission(self, request, view, obj):
        # Allow read-only access to any request SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS').
        if request.method in permissions.SAFE_METHODS:
            return True

        # For every other req method check if the authenticated user is the owner of the object.
        return obj.owner == request.user
