from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied


class OnlyAuthorModificationMixin(viewsets.ModelViewSet):
    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied('Удаление чужого контента запрещено!')
        instance.delete()

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        serializer.save()