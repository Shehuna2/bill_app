import requests

def process_payment(service_type, service_name, amount, phone_number=None):
    url = "https://api.opay.com/transaction/v1/service"
    headers = {
        "Authorization": "OPAYPRV17351582772620.012108487175019",
        "Content-Type": "application/json",
    }
    data = {
        "serviceType": service_type,
        "serviceName": service_name,
        "amount": amount,
    }
    if phone_number:
        data["phoneNumber"] = phone_number

    response = requests.post(url, headers=headers, json=data)
    return response.json()