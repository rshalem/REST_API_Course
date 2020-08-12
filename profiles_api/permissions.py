from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""

        if request.method in permissions.SAFE_METHODS:
            # safe_methods = GET, POST
            return True

        return obj.id == request.user.id
        # checking whether id matches if request.method not in SAFE_METHODS