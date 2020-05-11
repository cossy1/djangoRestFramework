from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    # Read permissions are allowed to any request,
    # so we'll always allow GET, HEAD or OPTIONS requests.

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        '''
        Only owners of an object have the permission
        to delete or update the object.
        '''
        return obj.owner == request.user
