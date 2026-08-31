from rest_framework.permissions import BasePermission


class IsOrganizer(BasePermission):
    """Allow access only to users with the 'organizer' role."""

    def has_permission(self, request, view):
        return bool(
            request.user
            and request.user.is_authenticated
            and request.user.role == "organizer"
        )
