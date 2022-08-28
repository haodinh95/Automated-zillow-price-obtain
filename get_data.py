from bs4 import BeautifulSoup
import requests


class Get_data:
    def __init__(self, link):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9'}
        self.link = link

    def get_htmldata(self):
        raw_data = requests.get(self.link, headers=self.headers)
        raw_data_to_txt = raw_data.text
        soup = BeautifulSoup(raw_data_to_txt, "html.parser")
        return soup

    def get_href(self, raw_data):
        empty_list = []
        for data in raw_data:
            link = data.get("href")
            empty_list.append(link)
        return empty_list

    def get_text(self, raw_data):
        empty_list = []
        for data in raw_data:
            link = data.getText()
            empty_list.append(link)
        return empty_list
