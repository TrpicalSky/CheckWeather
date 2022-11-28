import requests
from bs4 import BeautifulSoup

class ScrapeWeather:
    city = "Youngstown"
    url = "https://www.google.com/search?q="+"weather"+ city
    

    def __init__(self) -> None:
        self.temp = self.scrapeweather()

    def scrapeweather(self):
        html = requests.get(self.url).content
        soup = BeautifulSoup(html, 'html.parser')
        temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
        str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
        return temp
    
    def checkTemp(self):
        result = ''.join([i for i in self.temp if i.isdigit()])
        if int(result) >= 90:
            print(f"The current temp is {self.temp} and it is too hot")
        elif int(result) > 65 and int(result) < 90:
            print(f"The current temp is {self.temp} and it is just right")
        else:
            print(f"The current temp is {self.temp} and it is to cold")

