# scraper.py
import threading
import time

def scrape_articles():
    while True:
        # Implement your scraping logic here
        print("Scraping articles...")
        time.sleep(3600)  # Sleep for 1 hour

def start_scraping():
    threading.Thread(target=scrape_articles, daemon=True).start()
