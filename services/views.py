from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from .models import Service, Purchase
from wallet.models import Wallet


@login_required
def purchase_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    wallet = request.user.wallet

    if request.method == "POST":
        quantity = int(request.POST.get("quantity", 1))
        total_price = service.price * quantity

        if wallet.has_sufficient_balance(total_price):
            wallet.withdraw(total_price)
            Purchase.objects.create(
                user=request.user,
                service=service,
                quantity=quantity,
                total_price=total_price,
            )
            # Send notification email
            send_mail(
                subject="Purchase Successful",
                message=f"Dear {request.user.username},\n\nYou have successfully purchased {quantity} x {service.name} for ₦{total_price}.",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[request.user.email],
            )
            return render(request, "services/success.html", {"service": service, "quantity": quantity})
        else:
            return render(request, "services/failed.html", {"error": "Insufficient wallet balance."})

    return render(request, "services/purchase.html", {"service": service})
    
    
@login_required
def purchase_history(request):
    purchases = request.user.purchases.all().order_by('-purchased_at')
    
    return render(request, "services/purchase_history.html", {"purchases": purchases})