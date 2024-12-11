import random
import uuid
from datetime import datetime, timedelta
from data import stores, items
from data import discount_description


def generate_receipt_data():
    def random_transaction_date():
        return (datetime.now() - timedelta(days=random.randint(0, 30))).strftime("%Y-%m-%d %H:%M:%S")

    def random_item():
        catalog_number = f'729{random.randint(1000000000, 9999999999)}'
        item_name = random.choice(items)
        unit_price = round(random.uniform(5, 50), 2)
        pricing_type = 'fixed'
        quantity = random.randint(1, 5)
        weight = round(random.uniform(0.5, 3.0), 2) if pricing_type == "weight-based" else None
        total_price = round(unit_price * (weight if weight else quantity), 2)

        return {
            "itemName": item_name,
            "quantity": quantity,
            "unitPrice": unit_price,
            "totalPrice": total_price,
            "catalogNumber": catalog_number,
            "pricingType": pricing_type,
            "weightDetails": {
                "weight": weight,
                "weightUnit": "kg" if weight else None
            }
        }

    def random_discount():
        return {
            "description": random.choice(discount_description),
            "amount": round(-random.uniform(2, 20), 2)
        }

    receipt_data = {
        "receiptId": str(uuid.uuid4()),
        "storeInformation": random.choice(stores),
        "transactionDetails": {
            "transactionDate": random_transaction_date(),
            "totalAmount": 0,
            "currency": "ILS"
        },
        "itemDetails": [],
        "discounts": []
    }

    num_items = random.randint(5, 15)
    total_amount = 0
    for _ in range(num_items):
        item = random_item()
        receipt_data["itemDetails"].append(item)
        total_amount += item["totalPrice"]

    num_discounts = random.randint(0, 3)
    discounts_total = 0
    for _ in range(num_discounts):
        discount = random_discount()
        receipt_data["discounts"].append(discount)
        discounts_total += discount["amount"]

    receipt_data["transactionDetails"]["totalAmount"] = round((total_amount - discounts_total), 2)

    return receipt_data


sample_receipt = generate_receipt_data()
print(sample_receipt)
