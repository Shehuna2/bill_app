from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .opay_integration import initialize_opay_payment, verify_opay_payment

@login_required
def wallet_dashboard(request):
    wallet = request.user.wallet
    transactions = wallet.transactions.all().order_by('-created_at')
    return render(request, "wallet/dashboard.html", {"wallet": wallet, "transactions": transactions})

@login_required
def deposit_view(request):
    if request.method == "POST":
        amount = float(request.POST["amount"])
        deposit_url = initialize_opay_payment(request.user, amount)
        return redirect(deposit_url)
    return render(request, "wallet/deposit.html")

@login_required
def verify_deposit_view(request):
    reference = request.GET.get("reference")
    wallet = request.user.wallet
    if verify_opay_payment(reference, wallet):
        return render(request, "wallet/success.html")
    else:
        return render(request, "wallet/failed.html")
