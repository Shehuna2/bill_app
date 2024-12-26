import requests

SECRET_KEY = "your-opay-secret-key"

def initialize_opay_payment(user, amount):
    url = "https://api.opayweb.com/api/v3/payments/pay"
    headers = {
        "Authorization": f"Bearer {YOUR_SECRET_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "amount": int(amount * 100),  # Amount in kobo
        "reference": f"DEP{user.id}{int(amount * 1000)}",
        "currency": "NGN",
        "returnUrl": "https://yourapp.com/wallet/deposit/verify/",
        "callbackUrl": "https://yourapp.com/wallet/deposit/callback/",
        "user": {
            "name": user.username,
            "email": user.email,
        },
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200 and response.json().get("code") == "00000":
        return response.json()["data"]["cashierUrl"]
    else:
        raise Exception("Opay initialization failed!")

def verify_opay_payment(reference, wallet):
    url = "https://api.opayweb.com/api/v3/transaction/status"
    headers = {
        "Authorization": f"Bearer {YOUR_SECRET_KEY}",
        "Content-Type": "application/json",
    }
    payload = {"reference": reference}
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200 and response.json().get("data")["status"] == "SUCCESS":
        amount = response.json()["data"]["amount"] / 100  # Convert from kobo to Naira
        wallet.deposit(amount)
        return True
    return False
