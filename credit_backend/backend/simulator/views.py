from django.http import JsonResponse
import json
from backend.simulator.utils import calculate_credit_score
from backend.simulator.models import CreditScore  # ✅ Import CreditScore model
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

def safe_int(value, default=0):
    """ Convert value to int safely, return default if invalid. """
    try:
        return int(value) if value is not None and str(value).strip() != "" else default
    except ValueError:
        return default  # If conversion fails, return default

@api_view(["POST"]) 
@permission_classes([IsAuthenticated])  # ✅ Require authentication
def credit_score_simulation(request):
    try:
        # ✅ Get user from authentication
        user = request.user

        # Parse JSON data from request
        data = json.loads(request.body.decode("utf-8"))

        processed_data = {
            "emi_payment": data.get("emi_payment"),
            "credit_usage": safe_int(data.get("credit_usage")),
            "credit_limit": safe_int(data.get("credit_limit")),
            "num_credit_cards": safe_int(data.get("num_credit_cards")),
            "credit_mix": data.get("credit_mix"),
            "hard_inquiries": safe_int(data.get("hard_inquiries")),
            "credit_history_years": safe_int(data.get("credit_history_years")),
            "monthly_debt": safe_int(data.get("monthly_debt")),
            "monthly_income": safe_int(data.get("monthly_income")),
        }

        # Debugging - Print received data
        print("✅ Received Data:", processed_data)

        # Check for critical missing values
        if processed_data["credit_limit"] == 0 or processed_data["monthly_income"] == 0:
            return JsonResponse({"error": "Invalid input values. Credit limit and income are required."}, status=400)

        # ✅ Calculate credit score
        score = calculate_credit_score(processed_data)

        # ✅ Store the credit score in the database
        CreditScore.objects.create(
            user=user,
            emi_payment=processed_data["emi_payment"],
            credit_usage=processed_data["credit_usage"],
            credit_limit=processed_data["credit_limit"],
            num_credit_cards=processed_data["num_credit_cards"],
            credit_mix=processed_data["credit_mix"],
            hard_inquiries=processed_data["hard_inquiries"],
            credit_history=processed_data["credit_history_years"],
            monthly_debt=processed_data["monthly_debt"],
            monthly_income=processed_data["monthly_income"],
            credit_score=score,
        )

        return JsonResponse({"credit_score": score, "message": "Credit score calculated and saved successfully!"})

    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON format."}, status=400)
    except Exception as e:
        print(f"Error: {e}") 
        return JsonResponse({"error": "An error occurred while processing your request."}, status=500)
