import pandas as pd
import time
import random
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class NeweggScraper:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless") 
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")
        
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        self.results = []
        self.seen_names = set()

    def scrape_category(self, search_query, max_pages=1):
        for page in range(1, max_pages + 1):
            print(f"[*] Scraping Page {page} for: {search_query}...")
            url = f"https://www.newegg.com/p/pl?d={search_query}&page={page}"
            self.driver.get(url)

            try:
                # Tunggu kontainer produk muncul
                WebDriverWait(self.driver, 15).until(
                    EC.presence_of_all_elements_located((By.CLASS_NAME, "item-container"))
                )
                
                # OPTIMASI: Scroll lebih lambat agar JavaScript merender deskripsi & gambar
                total_height = int(self.driver.execute_script("return document.body.scrollHeight"))
                for i in range(1, total_height, 800):
                    self.driver.execute_script(f"window.scrollTo(0, {i});")
                    time.sleep(0.3)
                
                time.sleep(2) # Buffer tambahan setelah scroll selesai

                items = self.driver.find_elements(By.CLASS_NAME, "item-container")

                for item in items:
                    try:
                        name = item.find_element(By.CLASS_NAME, "item-title").text
                        
                        if not name or name in self.seen_names:
                            continue
                        
                        # Ekstraksi Harga
                        try:
                            price = item.find_element(By.CLASS_NAME, "price-current").text.replace('\n', '').strip()
                        except:
                            price = "Price not listed"

                        # Ekstraksi Gambar
                        try:
                            image_url = item.find_element(By.TAG_NAME, "img").get_attribute("src")
                        except:
                            image_url = "N/A"

                        # --- PERBAIKAN DESKRIPSI (Fallback Mechanism) ---
                        description = "N/A"
                        # Coba selector 1: Bullet points (umum di list view)
                        bullets = item.find_elements(By.CLASS_NAME, "item-bullet-points")
                        # Coba selector 2: Features (umum di grid view)
                        features = item.find_elements(By.CLASS_NAME, "item-features")
                        
                        if bullets and bullets[0].text.strip():
                            description = bullets[0].text.replace('\n', ' | ')
                        elif features and features[0].text.strip():
                            description = features[0].text.replace('\n', ' | ')
                        # ------------------------------------------------

                        self.results.append({
                            "Product Name": name,
                            "Price": price,
                            "Image URL": image_url,
                            "Category": search_query,
                            "Description": description
                        })
                        
                        self.seen_names.add(name)

                    except Exception:
                        continue 

                time.sleep(random.uniform(2, 4))

            except Exception as e:
                print(f"[!] Timeout or Error on page {page}")
                break

    def export_data(self, filename="newegg_output"):
        if not self.results:
            print("[!] No data to save.")
            return

        df = pd.DataFrame(self.results)
        df.to_csv(f"{filename}.csv", index=False)
        
        with open(f"{filename}.json", 'w', encoding='utf-8') as f:
            json.dump(self.results, f, indent=4)
            
        print(f"[+] Done! Saved {len(self.results)} unique products to CSV and JSON.")

    def quit(self):
        self.driver.quit()

if __name__ == "__main__":
    scraper = NeweggScraper()
    try:
        # Contoh penggunaan: mencari "Monitor" sebanyak 1 halaman
        scraper.scrape_category("Monitor", max_pages=1)
        scraper.export_data()
    finally:
        scraper.quit()