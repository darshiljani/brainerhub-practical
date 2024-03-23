from app.models import Employee
from rest_framework import serializers


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            "employee_id",
            "first_name",
            "last_name",
            "phone_number",
            "salary",
            "manager",
            "department_id",
            "company",
        ]
