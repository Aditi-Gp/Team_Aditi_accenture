import pandas as pd
from datetime import datetime
from pathlib import Path

# Load inventory data
DATA_PATH = Path("data/inventory_monitoring.csv")

df = pd.read_csv(DATA_PATH)

def check_inventory(product_id: int, store_id: int) -> dict:
    inventory = df[(df["Product ID"] == product_id) & (df["Store ID"] == store_id)]

    if inventory.empty:
        return {"error": "Inventory data not found for the given Product ID and Store ID."}

    row = inventory.iloc[0]

    stock_level = row["Stock Levels"]
    reorder_point = row["Reorder Point"]
    stockout_freq = row["Stockout Frequency"]
    supplier_lead_time = row["Supplier Lead Time (days)"]
    expiry_date = datetime.strptime(row["Expiry Date"], "%d-%m-%Y")
    warehouse_capacity = row["Warehouse Capacity"]
    fulfillment_time = row["Order Fulfillment Time (days)"]

    today = datetime.today()
    days_until_expiry = (expiry_date - today).days

    reorder_needed = stock_level <= reorder_point

    insights = {
        "stock_level": stock_level,
        "reorder_point": reorder_point,
        "reorder_needed": reorder_needed,
        "stockout_risk": "High" if stockout_freq > 10 else "Low",
        "days_until_expiry": days_until_expiry,
        "supplier_lead_time": supplier_lead_time,
        "order_fulfillment_days": fulfillment_time,
        "warehouse_capacity": warehouse_capacity,
        "recommendation": "Reorder Now" if reorder_needed else "Sufficient Stock"
    }

    return insights

# Example usage
if __name__ == "__main__":
    result = check_inventory(9286, 16)
    print(result)
