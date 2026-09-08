import csv
import requests
from bs4 import BeautifulSoup

URL = "https://www.olx.com.pk/houses_c1721?page=1"

r = requests.get(URL)
soup = BeautifulSoup(r.content, "html5lib")

properties = []

# Dynamic listings ko article tag ya div ke zariye target kar rahe hain
cards = soup.find_all("article", class_="_65e508e1")

for card in cards:
    item = {}

    # 1. Title
    title_div = card.find("div", {"aria-label": "Title"})
    item["title"] = (
        title_div.get_text(strip=True) if title_div else "N/A"
    )

    # 2. Price
    price_div = card.find("div", {"aria-label": "Price"})
    item["Price"] = (
        price_div.get_text(strip=True) if price_div else "N/A"
    )

    # 3. Beds
    beds_span = card.find("span", {"aria-label": "Beds"})
    item["Beds"] = (
        beds_span.get_text(strip=True) if beds_span else "N/A"
    )

    # 4. Bathrooms
    baths_span = card.find("span", {"aria-label": "Bathrooms"})
    item["Bath rooms"] = (
        baths_span.get_text(strip=True) if baths_span else "N/A"
    )

    # 5. Area
    area_span = card.find("span", {"aria-label": "Area"})
    item["Area"] = (
        area_span.get_text(strip=True) if area_span else "N/A"
    )

    properties.append(item)

# Save to CSV
filename = "Week6_webscraping_beautifulsoup/olx_houses.csv"
with open(filename, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(
        f, fieldnames=["title", "Price", "Beds", "Bath rooms", "Area"]
    )
    writer.writeheader()
    writer.writerows(properties)

print(f"Successfully saved {len(properties)} properties to {filename}")





