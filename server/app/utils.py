import pandas as pd

from app.serializers.CompanySerializer import CompanySerializer
from app.serializers.EmployeeSerializer import EmployeeSerializer


def insert_data_from_excel(file_path):
    try:
        # Read Excel file
        df = pd.read_excel(file_path)

        # Validate required columns
        required_columns = [
            "COMPANY_NAME",
            "EMPLOYEE_ID",
            "FIRST_NAME",
            "LAST_NAME",
            "PHONE_NUMBER",
            "SALARY",
            "DEPARTMENT_ID",
            "MANAGER_ID",
        ]
        if not all(col in df.columns for col in required_columns):
            raise ValueError("Excel file is missing required columns")

        # Extract unique company names
        unique_companies = df["COMPANY_NAME"].unique()

        # Prepare company data
        company_data = [{"name": name} for name in unique_companies]

        # Create companies using serializer
        company_serializer = CompanySerializer(data=company_data, many=True)
        if company_serializer.is_valid():
            companies = company_serializer.save()
        else:
            raise ValueError(f"Error creating companies: {company_serializer.errors}")

        # Create a map/dictionary of company names to IDs
        company_id_map = {company.name: company.id for company in companies}

        # Prepare employee data
        employee_data = []
        for _, row in df.iterrows():
            company_id = company_id_map[row["COMPANY_NAME"]]
            employee_data.append(
                {
                    "employee_id": row["EMPLOYEE_ID"],
                    "first_name": row["FIRST_NAME"],
                    "last_name": row["LAST_NAME"],
                    "phone_number": row["PHONE_NUMBER"],
                    "company": company_id,
                    "salary": row["SALARY"],
                    "department_id": row["DEPARTMENT_ID"],
                    "manager": row["MANAGER_ID"],
                }
            )

        # Create employees using serializer
        employee_serializer = EmployeeSerializer(data=employee_data, many=True)
        if employee_serializer.is_valid():
            employee_serializer.save()
        else:
            raise ValueError(f"Error creating employees: {employee_serializer.errors}")

    except FileNotFoundError:
        raise FileNotFoundError("Excel file not found")
    except pd.errors.ParserError:
        raise ValueError("Invalid Excel file format")
    except Exception as e:
        raise RuntimeError(f"An error occurred: {str(e)}")
