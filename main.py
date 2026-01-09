import requests

class WebScraper:
  def __init__(self):
    self.base_url = "https://wiki.factorio.com"

  def grab_web_page(self, page):
    url = self.base_url + "/" + page.replace(' ', '_')
    response = requests.get(url)

    if response.status_code != 200:
      print(f'Error {response.status_code}: Cannot access url {url}')

    return response.text


if __name__ == '__main__':
  scraper = WebScraper()
  scraper.grab_web_page("Tungsten Plate")
