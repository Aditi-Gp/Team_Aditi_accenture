# # llm_agent.py — Explains agent decisions using Ollama on-prem LLMs

# import requests

# OLLAMA_URL = "http://localhost:11434/api/generate"
# MODEL_NAME = "llama3"  # Change to the model you're using in Ollama

# # Prompt templates for different agents
# PROMPT_TEMPLATES = {
#     "demand": "Explain why the demand prediction for product ID {product_id} is what it is. Consider seasonality, promotions, trends, and external factors.",
#     "inventory": "Explain the inventory status for product ID {product_id}. Include reorder needs, stockouts, lead time, and warehouse capacity.",
#     "pricing": "Explain the pricing strategy for product ID {product_id}. Include factors like competitor pricing, sales, discounts, and return rates."
# }

# def ask_ollama(prompt):
#     try:
#         response = requests.post(OLLAMA_URL, json={
#             "model": MODEL_NAME,
#             "prompt": prompt,
#             "stream": False
#         })
#         result = response.json()
#         return {"explanation": result.get("response", "No response from LLM")}
#     except Exception as e:
#         return {"error": str(e)}

# def explain_decision(agent: str, product_id: int):
#     if agent not in PROMPT_TEMPLATES:
#         return {"error": "Unknown agent type"}
#     prompt = PROMPT_TEMPLATES[agent].format(product_id=product_id)
#     return ask_ollama(prompt)

# agents/llm_agent.py

import os

# Flag to detect deployment
IS_DEPLOYMENT = os.getenv("ENV", "dev") == "production"

def query_llm(prompt: str) -> str:
    if IS_DEPLOYMENT:
        # Mocked response for deployment
        return (
            "🧠 [MOCK LLM RESPONSE]\n"
            "Based on the demand, inventory, customer segment, and price trends, "
            "you should restock this product moderately and consider a 10% discount for regular customers."
        )
    
    # On-prem Ollama code (only for local use)
    try:
        from ollama import Client
        client = Client(host="http://localhost:11434")  # Update if needed
        response = client.chat(model="llama3", messages=[{"role": "user", "content": prompt}])
        return response['message']['content']
    except Exception as e:
        return f"Error calling local LLM: {e}"
