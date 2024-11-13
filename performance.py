import requests
import time
import pandas as pd
import matplotlib.pyplot as plt

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


# Function to test site performance
def test_site_performance(site_name, url):
    try:
        # Start the timer
        start_time = time.time()

        # Send a GET request to the website
        response = requests.get(url)

        # End the timer
        end_time = time.time()

        # Calculate the total response time
        response_time = end_time - start_time

        return response_time

    except requests.exceptions.RequestException:
        # If error occurs, return None
        return None


# List to store the results
results = []

# Run performance tests
for site_name, url in ecommerce_sites.items():
    response_time = test_site_performance(site_name, url)
    if response_time:
        results.append([site_name, response_time])

# Create a DataFrame from the results
df = pd.DataFrame(results, columns=["App Name", "Response Time (s)"])

# Save the DataFrame to an Excel file
df.to_excel("ecommerce_performance.xlsx", index=False, sheet_name='Performance')

# Plotting the data for visualization
plt.figure(figsize=(10, 6))
plt.bar(df["App Name"], df["Response Time (s)"], color='skyblue')
plt.xlabel('App Name')
plt.ylabel('Response Time (s)')
plt.title('Response Time of E-commerce Websites')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Save the plot as an image
plt.savefig("ecommerce_performance_chart.png")

# Display paths of the files
print("Excel sheet and chart saved as 'ecommerce_performance.xlsx' and 'ecommerce_performance_chart.png'")
