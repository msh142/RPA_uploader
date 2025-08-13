import pandas as pd
from playwright.sync_api import sync_playwright

# Load Excel data
df = pd.read_excel("gSearch.xlsx")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto("https://www.google.com")

    for index, row in df.iterrows():
        print(f"Searching for: {row['Items']}")

        # Fill search box
        page.fill("#APjFqb", str(row["Items"]))
        page.keyboard.press("Enter")  # Simulate pressing Enter

        page.wait_for_timeout(2000)  # Wait for results to load

    print("✅ All searches completed.")
    browser.close()
