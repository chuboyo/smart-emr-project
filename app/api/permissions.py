
from rest_framework import permissions, status


from rest_framework.response import Response


class IsDoctor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_doctor:
            return True
        else:
            Response(status=status.HTTP_403_FORBIDDEN)