from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time
import numpy as np

# ===== SETUP =====
URL = "https://www.amazon.com/s?k=mobile+phones"
CHROME_PATH = r"C:\chromedriver-win64\chromedriver.exe"

options = Options()
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--start-maximized")

# Bot detection se bachne ke liye essential flags
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

# Realistic User Agent
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
)

driver = webdriver.Chrome(service=Service(CHROME_PATH), options=options)
wait = WebDriverWait(driver, 15)

# Driver Script Injection (to hide selenium fingerprint)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

driver.get(URL)

# ===== CSV SETUP =====
with open("amazon_mobiles.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow([
        "product_name", "price",
        "reviews", "rating", "image_link", "product_link"
    ])

    # ===== SCRAPING =====
    for page in range(1, 6):
        print(f"Scraping Page {page}...")

        time.sleep(3)
        # Smooth Scroll (Lazy loading elements fetch karne ke liye)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        # Detect Products
        products = driver.find_elements(By.XPATH, '//div[@data-component-type="s-search-result"]')

        if not products:
            print("Page Empty or Amazon gives Block/CAPTCHA . Saving Debug Screen...")
            driver.save_screenshot(f"debug_page_{page}.png")
            break

        print(f"Found {len(products)} products on page {page}")

        # ===== EXTRACT DATA =====
        for product in products:
            # product_name
            try:
                product_name = product.find_element(By.XPATH, './/h2//span').text.strip()
            except:
                product_name = np.nan

            # price (textContent use karna hidden elements ke liye behtar hota hai)
            try:
                price = product.find_element(By.XPATH, './/span[@class="a-offscreen"]').get_attribute("textContent").strip()
            except:
                price = np.nan

            # reviews
            try:
                raw_reviews = product.find_element(By.XPATH, './/span[contains(@aria-label, "ratings")]/following-sibling::span').get_attribute("textContent")
                reviews = raw_reviews.replace("(", "").replace(")", "").strip()
            except:
                reviews = np.nan

            # rating
            try:
                rating = product.find_element(By.XPATH, './/span[contains(@aria-label, "out of 5 stars")]').get_attribute("aria-label").split(" ")[0]
            except:
                rating = np.nan

            # image
            try:
                img = product.find_element(By.CSS_SELECTOR, "img.s-image")
                image_link = img.get_attribute("src")
            except:
                image_link = np.nan

            # link
            try:
                link_elem = product.find_element(By.XPATH, './/h2/a')
                product_link = link_elem.get_attribute("href")
            except:
                product_link = np.nan

            writer.writerow([product_name, price, reviews, rating, image_link, product_link])

        # ===== NEXT PAGE =====
        try:
            next_btn = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a.s-pagination-next"))
            )
            driver.execute_script("arguments[0].click();", next_btn)
            time.sleep(4)
        except Exception as e:
            print("No more pages available ")
            break

driver.quit()
print("Process Complete! File saved: amazon_mobiles.csv ")