import requests
from bs4 import BeautifulSoup


class BMSScraper:
  def __init__(self, url='https://results.bmsce.in/'):
    self.url = url
  
  def scrape(self):
    try:
      req = requests.get(self.url)
    except:
      return None
    soup = BeautifulSoup(req.text, 'html.parser')
    results_soup = soup.find_all('a', class_='resultLink')
    results = [(result_soup.text, result_soup.get('href')) for result_soup in results_soup]
    return results