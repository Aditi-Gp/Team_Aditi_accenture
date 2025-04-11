import pandas as pd
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), "../data/demand_forecasting.csv")

def segment_for_product(product_id: int, store_id: int) -> str:
    try:
        df = pd.read_csv(DATA_PATH)
        
        # Filter for the specific product and store
        filtered = df[(df["Product ID"] == product_id) & (df["Store ID"] == store_id)]
        
        if filtered.empty:
            return "No customer data found for the given product-store combination."

        # Count the segment distribution
        segment_counts = filtered["Customer Segments"].value_counts().to_dict()
        dominant_segment = max(segment_counts, key=segment_counts.get)

        response = {
            "dominant_segment": dominant_segment,
            "segment_distribution": segment_counts
        }

        return f"Dominant Segment: {dominant_segment} | Distribution: {segment_counts}"

    except Exception as e:
        return f"Error in segment_for_product: {str(e)}"
