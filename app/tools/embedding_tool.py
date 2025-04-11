import requests

# Example for an Ollama embedding endpoint (adjust if your local Ollama server differs)
OLLAMA_EMBED_URL = "http://localhost:11434/api/embeddings"

def generate_embedding(text: str, model: str = "nomic-embed-text") -> list:
    payload = {
        "model": model,
        "prompt": text
    }
    response = requests.post(OLLAMA_EMBED_URL, json=payload)

    if response.status_code == 200:
        embedding = response.json().get("embedding")
        return embedding
    else:
        raise Exception(f"[Embedding Error] Ollama returned {response.status_code}: {response.text}")
