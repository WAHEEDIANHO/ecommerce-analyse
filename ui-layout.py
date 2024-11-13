from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time
import pandas as pd

# List of e-commerce websites to test
ecommerce_sites = {
    "Vinted": "https://www.vinted.com",
    "Zalando": "https://www.zalando.com",
    "Jumia": "https://www.jumia.com.ng",
    "Takealot": "https://www.takealot.com",
    "Konga": "https://www.konga.com",
    "Amazon": "https://www.amazon.com",
    "Walmart": "https://www.walmart.com",
    "Alibaba": "https://www.alibaba.com",
    "Flipkart": "https://www.flipkart.com",
    "Rakuten": "https://www.rakuten.com"
}

# Function to ensure element is clickable
def click_element(driver, element):
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(1)  # Wait for the element to be in view
    try:
        element.click()
    except ElementClickInterceptedException:
        driver.execute_script("arguments[0].click();", element)

# Function to simulate usability testing
def usability_test(site_name, url, driver):
    driver.get(url)

    # Record page load time
    start_time = time.time()
    driver.get(url)
    load_time = time.time() - start_time

    # Check for Search bar visibility
    try:
        search_bar = driver.find_element(By.NAME, "q")  # Modify this based on each site
        search_bar_visible = search_bar.is_displayed()
    except NoSuchElementException:
        search_bar_visible = False

    # Simulate adding an item to the cart (this will vary per site)
    try:
        product = driver.find_element(By.CSS_SELECTOR, "a[href*='/product']")
        click_element(driver, product)
        time.sleep(2)

        add_to_cart = driver.find_element(By.CSS_SELECTOR, "button[class*='add-to-cart']")
        click_element(driver, add_to_cart)
        item_added = True
    except NoSuchElementException:
        item_added = False

    # Simulate navigating to the cart page
    try:
        cart_button = driver.find_element(By.CSS_SELECTOR, "a[href*='/cart']")
        click_element(driver, cart_button)
        time.sleep(2)
        cart_loaded = True
    except NoSuchElementException:
        cart_loaded = False

    # Collect usability data for the site
    return {
        "Site": site_name,
        "Load Time (s)": round(load_time, 2),
        "Search Bar Visible": search_bar_visible,
        "Item Added to Cart": item_added,
        "Cart Loaded": cart_loaded
    }

# Initialize Selenium WebDriver (e.g., Chrome)
driver_path = "/usr/local/bin/chromedriver"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")  # Run headless browser
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

service = ChromeService(executable_path=driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# List to store usability test results
results = []

# Run usability tests on each e-commerce website
for site_name, url in ecommerce_sites.items():
    result = usability_test(site_name, url, driver)
    results.append(result)

# Close the browser
driver.quit()

# Create a DataFrame from the results
df = pd.DataFrame(results)

# Save the results to an Excel file
df.to_excel("ecommerce_usability_testing.xlsx", index=False)

# Display the DataFrame
print(df)