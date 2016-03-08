from rest_framework import permissions, viewsets
from rest_framework.response import Response

from .models import Department
from .permissions import IsAuthorOfPost
from .serializers import DepartmentSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.order_by('-created_at')
    serializer_class = DepartmentSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)
        return (permissions.IsAuthenticated(), IsAuthorOfPost(),)

def perform_create(self, serializer):
    instance = serializer.save(author=self.request.user)

    return super(DepartmentViewSet, self).perform_create(serializer)



class AccountDepartmentsViewSet(viewsets.ViewSet):
    queryset = Department.objects.select_related('author').all()
    serializer_class = DepartmentSerializer

    def list(self, request, account_username=None):
        queryset = self.queryset.filter(author__username=account_username)
        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data)
