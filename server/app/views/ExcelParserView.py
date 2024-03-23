from app.utils import insert_data_from_excel
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class ExcelInputAPI(APIView):
    def post(self, request):
        try:
            excel_file = request.data.get("file")
            if not excel_file:
                return Response(
                    {"error": "File is not provided"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            insert_data_from_excel(excel_file)
            return Response(
                {"message": "Data inserted successfully"},
                status=status.HTTP_201_CREATED,
            )
        except FileNotFoundError:
            return Response(
                {"error": "Excel file not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except ValueError as ve:
            return Response({"error": str(ve)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
