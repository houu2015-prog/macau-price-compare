import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def get_price_sanmiao(keyword: str):
    url = f"http://www.sanmio.com.mo/search?q={keyword}"
    try:
        resp = requests.get(url, headers=HEADERS, timeout=10)
        resp.raise_for_status()
    except Exception as e:
        print("新苗請求失敗：", e)
        return None

    soup = BeautifulSoup(resp.text, "html.parser")

    item = soup.select_one(".item")  # TODO: 修改 selector
    if not item:
        return None

    name_el = item.select_one(".name")
    price_el = item.select_one(".value")

    if not name_el or not price_el:
        return None

    name = name_el.get_text(strip=True)
    price = price_el.get_text(strip=True)

    return {
        "supermarket": "新苗",
        "name": name,
        "price": price
    }

