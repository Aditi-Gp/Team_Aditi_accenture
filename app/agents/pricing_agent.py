import pandas as pd
from sklearn.linear_model import LinearRegression
from pathlib import Path

# Load pricing data
DATA_PATH = Path("data/pricing_optimization.csv")

df = pd.read_csv(DATA_PATH)

def optimize_price_for_product(product_id: int, store_id: int) -> dict:
    # Filter data for the specific product and store
    product_data = df[(df["Product ID"] == product_id) & (df["Store ID"] == store_id)]

    if product_data.empty:
        return {"error": "No pricing data available for this product/store"}

    row = product_data.iloc[0]
    
    base_price = row["Price"]
    competitor_price = row["Competitor Prices"]
    elasticity = row["Elasticity Index"]
    return_rate = row["Return Rate (%)"]
    discount = row["Discounts"]
    storage_cost = row["Storage Cost"]

    # Simple rule-based pricing logic
    new_price = base_price

    if competitor_price < base_price:
        new_price = competitor_price - (0.05 * base_price)  # offer slight advantage

    if elasticity > 1.5:
        new_price *= 0.95  # customers are more price sensitive

    if return_rate > 10:
        new_price *= 1.02  # increase price slightly to offset return loss

    if storage_cost > 7:
        new_price *= 0.98  # reduce price to push sales and clear storage

    recommendation = {
        "original_price": base_price,
        "competitor_price": competitor_price,
        "adjusted_price": round(new_price, 2),
        "elasticity_index": elasticity,
        "storage_cost": storage_cost,
        "return_rate": return_rate,
        "strategy": "Price optimized based on market and cost signals."
    }

    return recommendation

# Example usage
if __name__ == "__main__":
    result = optimize_price_for_product(9502, 13)
    print(result)
