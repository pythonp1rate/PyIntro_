import requests
from bs4 import BeautifulSoup

class QuoteScraper:
    """A class designed to scrape quotes from quotes.toscrape.com."""
    
    def __init__(self, base_url):
        self.base_url = base_url
        self.all_data = []

    def _fetch_page(self, url):
        """Private method to fetch and parse HTML."""
        try:
            response = requests.get(url)
            response.raise_for_status() # Check for bad status codes
            return BeautifulSoup(response.text, 'html.parser')
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None

    def scrape_page(self, page_num):
        """Scrapes data from a single, numbered page."""
        url = f'{self.base_url}/page/{page_num}/'
        soup = self._fetch_page(url)
        
        if not soup:
            return [] # Return empty list on error

        # The below code you could modify to suit your needs
        page_quotes = []
        for quote in soup.find_all('div', class_='quote'):
            text = quote.find('span', class_='text').text.strip().replace('“', '').replace('”', '')
            author = quote.find('small', class_='author').text
            page_quotes.append({'author': author, 'quote': text, 'page': page_num})
            
        return page_quotes

    def run_scraper(self, max_pages=5):
        """Runs the scraper for a specified number of pages."""
        print(f"Starting scrape for up to {max_pages} pages...")
        for page in range(1, max_pages + 1):
            data = self.scrape_page(page)
            if not data:
                print(f"No data found on page {page}. Stopping.")
                break # Stop if a page fails or is empty
            self.all_data.extend(data)
            print(f"Collected {len(data)} quotes from page {page}.")
        print(f"Scraping finished. Total quotes collected: {len(self.all_data)}")


# EXECUTION: The main script becomes clean and readable!
if __name__ == '__main__':
    scraper = QuoteScraper('http://quotes.toscrape.com')
    scraper.run_scraper(max_pages=2) # Only scrape the first two pages
    
    # Example: print the data
    for item in scraper.all_data:
        print(f"[{item['page']}] {item['author']}: {item['quote'][:50]}...")