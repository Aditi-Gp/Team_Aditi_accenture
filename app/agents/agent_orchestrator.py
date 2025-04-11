# agents/agent_orchestrator.py — Central orchestrator coordinating all agents

from agents.llm_agent import query_llm
from agents.demand_agent import forecast_demand
from agents.inventory_agent import check_stock_levels, suggest_restock_action
from agents.pricing_agent import optimize_price_for_product
from agents.customer_agent import segment_for_product

def orchestrate(product_id: int, store_id: int):
    print(" [Orchestrator] Initiating multi-agent pipeline...")

    # Step 1: Demand Forecasting
    print(" [1] Forecasting demand...")
    demand_info = forecast_demand(product_id, store_id)

    # Step 2: Inventory Monitoring
    print(" [2] Checking inventory levels...")
    inventory_info = check_stock_levels(product_id, store_id)
    restock_suggestion = suggest_restock_action(product_id, store_id)

    # Step 3: Customer Intelligence
    print(" [3] Segmenting customers...")
    customer_info = segment_for_product(product_id, store_id)

    # Step 4: Pricing Optimization
    print(" [4] Optimizing price...")
    price_info = optimize_price_for_product(product_id, store_id)

    # Step 5: LLM Agent for Plan Recommendation
    print(" [5] Using LLM to synthesize insights and recommend actions...")
    llm_context = (
        f"Demand Forecast:\n{demand_info}\n\n"
        f"Inventory Info:\n{inventory_info}\n\n"
        f"Restock Suggestion:\n{restock_suggestion}\n\n"
        f"Customer Insights:\n{customer_info}\n\n"
        f"Pricing Optimization:\n{price_info}\n\n"
    )

    llm_plan = query_llm(
        f"As an inventory management expert, analyze the following retail data for Product {product_id} at Store {store_id} "
        f"and generate a recommended action plan:\n\n{llm_context}"
    )

    return {
        "demand_forecast": demand_info,
        "inventory_status": inventory_info,
        "restock_suggestion": restock_suggestion,
        "customer_segment": customer_info,
        "price_recommendation": price_info,
        "llm_summary": llm_plan,
    }

# For local testing
if __name__ == "__main__":
    test_product_id = 4277
    test_store_id = 48

    output = orchestrate(test_product_id, test_store_id)

    for key, value in output.items():
        print(f"\n🔹 {key.upper()} 🔹\n{value}")
