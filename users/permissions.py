from rest_framework import permissions
from rest_framework.views import Request, View


class IsAuthenticatedAndOwnerOrEmployee(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj) -> bool:
        return (
            request.user.is_authenticated
            and request.user.is_employee
            or request.user.is_authenticated
            and request.user == obj
        )
