import requests
from bs4 import BeautifulSoup

def scrape_competitor_price(product_name: str) -> float:
    url = f"https://www.example.com/search?q={product_name.replace(' ', '+')}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception("Failed to fetch competitor site")

    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Dummy parsing logic (replace with actual logic based on target site)
    price_tag = soup.find("span", {"class": "price"})
    if price_tag:
        return float(price_tag.text.strip().replace('$', ''))
    else:
        return -1.0  # Return -1 if not found
