from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

class WebDriverManager:
    def __init__(self, driver_path="chromedriver.exe"):
        self.options = Options()
        self.service = Service(driver_path)
        self.driver = webdriver.Chrome(service=self.service, options=self.options)
    
    def get_driver(self):
        return self.driver
    
    def close_driver(self):
        self.driver.quit()

class CreditCardScraper:
    def __init__(self, url, driver):
        self.url = url
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
    
    def fetch_page(self):
        self.driver.get(self.url)
    
    def get_elements_text(self, xpath):
        try:
            elements = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath)))
            return [element.text.strip() for element in elements]
        except:
            return []
    
    def extract_card_details(self):
        card_names = self.get_elements_text("//a[@class='title_list_link']")
        best_suited_for = self.get_elements_text("//h4[contains(text(), 'Best Suited For')]/following-sibling::p")
        reward_type = self.get_elements_text("//h4[contains(text(), 'Reward Type')]/following-sibling::p")
        welcome_benefits = self.get_elements_text("//h4[contains(text(), 'Welcome Benefits')]/following-sibling::div")
        
        fees_sections = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'fees-subpart')]")))
        joining_fees, renewal_fees = self.extract_fees(fees_sections)
        
        return self.format_card_data(card_names, joining_fees, renewal_fees, best_suited_for, reward_type, welcome_benefits)
    
    def extract_fees(self, sections):
        joining_fees, renewal_fees = [], []
        for section in sections:
            joining_fees.append(self.get_fee_text(section, "Joining Fee"))
            renewal_fees.append(self.get_fee_text(section, "Renewal Fee"))
        return joining_fees, renewal_fees
    
    def get_fee_text(self, section, fee_type):
        try:
            return section.find_element(By.XPATH, f".//h4[contains(text(), '{fee_type}')]/following-sibling::div").text.strip()
        except:
            return "N/A"
    
    def format_card_data(self, names, join_fees, renew_fees, suited_for, rewards, benefits):
        num_cards = len(names)
        join_fees += ["N/A"] * (num_cards - len(join_fees))
        renew_fees += ["N/A"] * (num_cards - len(renew_fees))
        suited_for += ["N/A"] * (num_cards - len(suited_for))
        rewards += ["N/A"] * (num_cards - len(rewards))
        benefits += ["N/A"] * (num_cards - len(benefits))
        
        return [
            [names[i], join_fees[i], renew_fees[i], suited_for[i], rewards[i], benefits[i]]
            for i in range(num_cards)
        ]

class DataSaver:
    @staticmethod
    def save_to_csv(data, filename="credit_cards.csv"):
        df = pd.DataFrame(data, columns=["Card Name", "Joining Fee", "Renewal Fee", "Best Suited For", "Reward Type", "Welcome Benefits"])
        df.to_csv(filename, index=False)
        print(f"Data saved to {filename}")

class BankScraperManager:
    def __init__(self, bank_urls, driver_manager):
        self.bank_urls = bank_urls
        self.driver_manager = driver_manager
    
    def scrape_all_banks(self):
        driver = self.driver_manager.get_driver()
        for bank_name, url in self.bank_urls.items():
            print(f"Scraping {bank_name}...")
            scraper = CreditCardScraper(url, driver)
            scraper.fetch_page()
            card_data = scraper.extract_card_details()
            DataSaver.save_to_csv(card_data, f"{bank_name}_credit_cards.csv")
        self.driver_manager.close_driver()

if __name__ == "__main__":
    bank_urls = {
        "AmericanExpress": "https://cardinsider.com/american-express/",
        "AU_Bank": "https://cardinsider.com/au-bank/",
        "Axis_Bank": "https://cardinsider.com/axis-bank/",
        "Bank_of_Baroda": "https://cardinsider.com/bank-of-baroda/",
        "HDFC_Bank": "https://cardinsider.com/hdfc-bank/",
        "HSBC": "https://cardinsider.com/hsbc/",
        "ICICI_Bank": "https://cardinsider.com/icici-bank/",
        "IndusInd_Bank": "https://cardinsider.com/indusind-bank/",
        "Kotak_Mahindra_Bank": "https://cardinsider.com/kotak-mahindra-bank/",
        "RBL_Bank": "https://cardinsider.com/rbl-bank/",
        "SBI_Card": "https://cardinsider.com/sbi/",
        "Standard_Chartered": "https://cardinsider.com/standard-chartered/",
        "Yes_Bank": "https://cardinsider.com/yes-bank/"
    }

    driver_manager = WebDriverManager()
    manager = BankScraperManager(bank_urls, driver_manager)
    manager.scrape_all_banks()
