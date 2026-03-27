
import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def get_price_lailai(keyword: str):
    url = f"https://www.royalsupermarket.com.mo/search?q={keyword}"
    try:
        resp = requests.get(url, headers=HEADERS, timeout=10)
        resp.raise_for_status()
    except Exception as e:
        print("來來請求失敗：", e)
        return None

    soup = BeautifulSoup(resp.text, "html.parser")

    item = soup.select_one(".product")  # TODO: 修改 selector
    if not item:
        return None

    name_el = item.select_one(".title")
    price_el = item.select_one(".price")

    if not name_el or not price_el:
        return None

    name = name_el.get_text(strip=True)
    price = price_el.get_text(strip=True)

    return {
        "supermarket": "來來",
        "name": name,
        "price": price
    }
