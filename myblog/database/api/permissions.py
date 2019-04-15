from rest_framework import permissions
class UserPermission(Permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj and request.method in SAFE_METHODS