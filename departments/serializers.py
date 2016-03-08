from rest_framework import serializers

from authentication.serializers import AccountSerializer
from .models import Department


class DepartmentSerializer(serializers.ModelSerializer):
    author = AccountSerializer(read_only=True, required=False)

    class Meta:
        model = Department

        fields = ('id', 'author', 'department_name', 'department_code', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')

    def get_validation_exclusions(self, *args, **kwargs):
        exclusions = super(DepartmentSerializer, self).get_validation_exclusions()

        return exclusions + ['author']

