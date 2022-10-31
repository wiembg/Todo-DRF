from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permissions(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        print(request.user)
        return obj.owner == request.user
                #if obj.owner is equal to request.user it will return True, otherwise False:return the results belonging to the owner