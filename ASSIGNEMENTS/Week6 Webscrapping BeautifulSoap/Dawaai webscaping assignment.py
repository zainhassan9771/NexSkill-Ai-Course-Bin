import csv
import requests
from bs4 import BeautifulSoup

URL = "https://dawaai.pk/all-medicines/a"
r = requests.get(URL)
soup = BeautifulSoup(r.content, "html5lib")

medicines = []

cards = soup.find_all("div", class_="column col-xs-6 col-2 my-8")

for card in cards:
    item = {}

    # 1. Product Name
    name_tag = card.find("h2")
    item["name"] = name_tag.get_text(strip=True) if name_tag else "N/A"

    # 2. Company Name
    p_tags = card.find_all("p")
    item["company_name"] = (
        p_tags[0].get_text(strip=True) if len(p_tags) > 0 else "N/A"
    )

    # 3. Pack Size
    item["pack_size"] = (
        p_tags[1].get_text(strip=True) if len(p_tags) > 1 else "N/A"
    )

    # 4. Price
    price_tag = card.find("h4")
    if price_tag:
        item["price"] = (
            price_tag.contents[0].strip()
            if price_tag.contents
            else price_tag.get_text(strip=True)
        )
    else:
        item["price"] = "N/A"
    medicines.append(item)

# CSV File Save
filename = "Week6_webscraping_beautifulsoup/Dawaai.com.csv"
with open(filename, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(
        f, fieldnames=["name", "company_name", "pack_size", "price"]
    )
    writer.writeheader()
    writer.writerows(medicines)

print(f"Successfully saved {len(medicines)} medicines to {filename}")