from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Employee(models.Model):
    employee_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    manager = models.IntegerField()
    department_id = models.IntegerField()
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="employees"
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
