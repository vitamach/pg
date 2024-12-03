import logging
import time
import random
from playwright.sync_api import sync_playwright
from typing import List, Dict, Optional

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)

logger = logging.getLogger('FirmyScraper')

class FirmyScraper:
    def __init__(self):
        self.playwright = None
        self.browser = None
        self.context = None
        self.page = None

    def setup(self):
        try:
            self.playwright = sync_playwright().start()
            self.browser = self.playwright.chromium.launch(
                headless=True,
                args=['--no-sandbox']
            )
            self.context = self.browser.new_context(
                viewport={'width': 1920, 'height': 1080},
                user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/119.0.0.0 Safari/537.36'
            )
            self.page = self.context.new_page()
            self.page.set_default_timeout(30000)
            logger.info("Playwright setup completed successfully")
        except Exception as e:
            logger.error(f"Error during setup: {e}")
            self.cleanup()
            raise

    def scrape_page(self, url: str) -> List[Dict[str, str]]:
        companies = []
        try:
            logger.info(f"Navigating to {url}")
            
            # Navigate to the search URL
            self.page.goto(url)
            self.page.wait_for_load_state('networkidle')
            
            # Save initial state
            self.page.screenshot(path='initial_page.png')
            
            # Look for firms
            firms = self.page.query_selector_all('.firm')
            if not firms:
                logger.info("No firms found with '.firm' selector, trying alternative selectors...")
                firms = self.page.query_selector_all('.firmList > div')
            
            logger.info(f"Found {len(firms)} firms")
            
            for firm in firms:
                try:
                    company = self._extract_company_info(firm)
                    if company:
                        companies.append(company)
                        logger.info(f"Extracted company: {company['nazev']}")
                except Exception as e:
                    logger.error(f"Error extracting company info: {e}")
                    continue
                    
            return companies

        except Exception as e:
            logger.error(f"Error during scraping: {e}")
            self.page.screenshot(path='error.png')
            return companies

    def _extract_company_info(self, element) -> Optional[Dict[str, str]]:
        try:
            # Extract basic info
            name_elem = element.query_selector('.name, .title, h3')
            address_elem = element.query_selector('.address, .location')
            phone_elem = element.query_selector('.phone, .contact .tel')
            web_elem = element.query_selector('a.web')
            
            if not name_elem:
                return None
                
            # Get the text content
            name = name_elem.text_content().strip()
            address = address_elem.text_content().strip() if address_elem else 'N/A'
            phone = phone_elem.text_content().strip() if phone_elem else 'N/A'
            web = web_elem.get_attribute('href') if web_elem else 'N/A'
            
            return {
                'nazev': name,
                'adresa': address,
                'telefon': phone,
                'web': web
            }
            
        except Exception as e:
            logger.error(f"Error in company extraction: {e}")
            return None

    def cleanup(self):
        try:
            if self.browser:
                self.browser.close()
            if self.playwright:
                self.playwright.stop()
            logger.info("Cleanup completed successfully")
        except Exception as e:
            logger.error(f"Error during cleanup: {e}")

def main():
    scraper = FirmyScraper()
    try:
        scraper.setup()
        # Use the correct URL format for the Czech version
        url = "https://www.firmy.cz/detail/12845783-cru-servis-karvina-stare-mesto.html"
        
        print("Starting scraping...")
        results = scraper.scrape_page(url)
        
        if results:
            print(f"\nFound {len(results)} companies")
            for company in results:
                print("\n" + "-" * 50)
                print(f"Název: {company['nazev']}")
                print(f"Adresa: {company['adresa']}")
                print(f"Telefon: {company['telefon']}")
                print(f"Web: {company['web']}")
        else:
            print("No companies found - check error.png for debugging")
            
    except Exception as e:
        logger.error(f"Main execution error: {e}")
    finally:
        scraper.cleanup()

if __name__ == "__main__":
    main()