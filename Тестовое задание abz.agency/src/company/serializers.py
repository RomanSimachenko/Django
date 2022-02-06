from rest_framework import serializers
from . import models


class EmployeeSerializer(serializers.ModelSerializer):
    chief_name = serializers.CharField(source='chief.name')

    class Meta:
        model = models.Employee
        fields = ('id', 'fio', 'position',
                  'chief_name', 'join_date', 'salary',)
