from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
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
            return render(request, "services/success.html", {"service": service, "quantity": quantity})
        else:
            return render(request, "services/failed.html", {"error": "Insufficient wallet balance."})

    return render(request, "services/purchase.html", {"service": service})
