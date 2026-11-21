# sales_report.py
# Weekly sales report for Hanami Goods online shop.
# Written by: Sato (backend team)
#
# How to run:
#   python sales_report.py

# Orders from last week (2026-11-09 to 2026-11-15).
# In the real system this comes from the database.
# For now we copy it here by hand every Monday.
orders = [
    {"order_id": "A1001", "date": "2026-11-09", "item": "Ceramic Mug",     "price": 1800, "quantity": 2, "status": "completed"},
    {"order_id": "A1002", "date": "2026-11-09", "item": "Linen Tote Bag",  "price": 2400, "quantity": 1, "status": "completed"},
    {"order_id": "A1003", "date": "2026-11-10", "item": "Incense Set",     "price": 1200, "quantity": 3, "status": "cancelled"},
    {"order_id": "A1004", "date": "2026-11-10", "item": "Ceramic Mug",     "price": 1800, "quantity": 1, "status": "completed"},
    {"order_id": "A1005", "date": "2026-11-11", "item": "Furoshiki Cloth", "price": 3200, "quantity": 1, "status": "completed"},
    {"order_id": "A1006", "date": "2026-11-11", "item": "Linen Tote Bag",  "price": 2400, "quantity": 2, "status": "cancelled"},
    {"order_id": "A1007", "date": "2026-11-12", "item": "Chopstick Pair",  "price": 900,  "quantity": 4, "status": "completed"},
    {"order_id": "A1008", "date": "2026-11-12", "item": "Incense Set",     "price": 1200, "quantity": 1, "status": "completed"},
    {"order_id": "A1009", "date": "2026-11-13", "item": "Furoshiki Cloth", "price": 3200, "quantity": 2, "status": "completed"},
    {"order_id": "A1010", "date": "2026-11-13", "item": "Ceramic Mug",     "price": 1800, "quantity": 1, "status": "cancelled"},
    {"order_id": "A1011", "date": "2026-11-14", "item": "Chopstick Pair",  "price": 900,  "quantity": 2, "status": "completed"},
    {"order_id": "A1012", "date": "2026-11-14", "item": "Linen Tote Bag",  "price": 2400, "quantity": 1, "status": "completed"},
    {"order_id": "A1013", "date": "2026-11-15", "item": "Ceramic Mug",     "price": 1800, "quantity": 3, "status": "completed"},
    {"order_id": "A1014", "date": "2026-11-15", "item": "Incense Set",     "price": 1200, "quantity": 2, "status": "completed"},
]


def total_sales(orders):
    total = 0
    for order in orders:
        total = total + order["price"] * order["quantity"]
    return total


def main():
    total = total_sales(orders)
    print("=== Hanami Goods Weekly Sales Report ===")
    print("Period: 2026-11-09 to 2026-11-15")
    print(f"Total sales: {total} yen")


main()
