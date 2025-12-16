from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

from django.utils import timezone
from datetime import timedelta
import uuid
from django.http import HttpResponse


from .models import Subscription

import requests
from django.conf import settings




def subscribe_page(request):
    return render(request, "subscribe.html")



def create_checkout(request):
    plan = request.POST.get("plan")
    
    if plan == "weekly":
        amount = 500   # $5.00
        name = "Weekly Subscription"

    if plan == "monthly":
        amount = 1000   # $10.00
        name = "Monthly Subscription"
    else:
        amount = 10000  # $100.00
        name = "Yearly Subscription"

    url = f"{settings.SQUARE_API_BASE}/v2/online-checkout/payment-links"

    headers = {
        "Authorization": f"Bearer {settings.SQUARE_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "idempotency_key": str(uuid.uuid4()),
        "order": {
            "location_id": settings.SQUARE_LOCATION_ID,
            "line_items": [
                {
                    "name": name,
                    "quantity": "1",
                    "base_price_money": {
                        "amount": amount,
                        "currency": "USD"
                    }
                }
            ]
        },
        "checkout_options": {
            "redirect_url": request.build_absolute_uri("/success/")
        }
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        checkout_url = response.json()["payment_link"]["url"]
        return redirect(checkout_url)

    print(response.text)
    return redirect("/error/")



def signup_view(request):
    if request.method == "POST":
        user = User.objects.create_user(
            username=request.POST["username"],
            email=request.POST["email"],
            password=request.POST["password"]
        )
        login(request, user)
        return redirect("subscribe")
    return render(request, "signup.html")


def login_view(request):
    if request.method == "POST":
        user = authenticate(
            username=request.POST["username"],
            password=request.POST["password"]
        )
        if user:
            login(request, user)
            return redirect("dashboard")
    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect("login")





def payment_success(request):
    plan = request.session.get("plan")
    duration = request.session.get("duration")

    Subscription.objects.update_or_create(
        user=request.user,
        defaults={
            "plan": plan,
            "start_date": timezone.now(),
            "end_date": timezone.now() + timedelta(days=duration)
        }
    )

    return render(request, "success.html")



def payment_error(request):
    return render(request, "error.html")




def dashboard(request):
    subscription = Subscription.objects.filter(user=request.user).first()
    return render(request, "dashboard.html", {"subscription": subscription})


def process_payment(request):
    if request.method == "POST":
        plan = request.POST.get("plan")
        return HttpResponse(f"Payment processing started for {plan}")
    return redirect("subscribe")