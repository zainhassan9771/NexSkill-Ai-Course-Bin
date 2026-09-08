import pandas as pd
from bs4 import BeautifulSoup

file_path = "Week6_webscraping_beautifulsoup/Properties for Sale in UAE _ Bayut.com.html"  # Path change kar lein

with open(file_path, "r", encoding="utf-8") as file:
    soup1 = BeautifulSoup(file, "html.parser")
# Target Dynamic cards / listings 
products1 = soup1.find_all("li", attrs={"role": "article"})

# if not found li 
if not products1:
    products1 = soup1.find_all("article")
beds_list = []
baths_list = []
area_list = []
location_list = []
price_list = []

for product1 in products1:
    # 1. Number of Beds
    try:
        beds_span = product1.find("span", {"aria-label": "Beds"})
        beds = beds_span.get_text(strip=True) if beds_span else "N/A"
    except:
        beds = "N/A"

    # 2. Number of Baths
    try:
        baths_span = product1.find("span", {"aria-label": "Baths"})
        baths = baths_span.get_text(strip=True) if baths_span else "N/A"
    except:
        baths = "N/A"

    # 3. Area of property
    try:
        area_span = product1.find("span", {"aria-label": "Area"})
        area = area_span.get_text(strip=True) if area_span else "N/A"
    except:
        area = "N/A"

    # 4. Location of property
    try:
        location_div = product1.find("div", {"aria-label": "Location"})
        location = (
            location_div.get_text(strip=True) if location_div else "N/A"
        )
    except:
        location = "N/A"

    # 5. Price of property
    try:
        price_span = product1.find("span", {"aria-label": "Price"})
        price = price_span.get_text(strip=True) if price_span else "N/A"
    except:
        price = "N/A"

    # Lists me append kar rahe hain
    beds_list.append(beds)
    baths_list.append(baths)
    area_list.append(area)
    location_list.append(location)
    price_list.append(price)

# Pandas DataFrame Creation
bayut_df = pd.DataFrame({
    "Beds": beds_list,
    "Baths": baths_list,
    "Area": area_list,
    "Location": location_list,
    "Price": price_list,
})

# Save to CSV using Pandas
bayut_df.to_csv(
    "Week6_webscraping_beautifulsoup/payut_uae_property.csv", index=False
)
print("Data Saved Successfully!")