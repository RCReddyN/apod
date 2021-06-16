import os
import json
import requests
from datetime import date
from dotenv import load_dotenv
from PIL import Image
import PIL

load_dotenv()

class Apod:
    def __init__(self, date=str(date.today())):
        self.token = os.environ.get('nasa_token')
        self.date = date

    def get_url(self):
        return 'https://api.nasa.gov/planetary/apod?'
    
    def get_params(self):
        return {'api_key':self.token, 'date':self.date}
    
    def get_image(self):
        r = requests.get(url=self.get_url(), params=self.get_params())
        return r.json()

instance = Apod(input())
img_data = instance.get_image()
img_url = img_data["url"]
page = requests.get(img_url)
with open('./img/apod.jpg', 'wb') as f:
    f.write(page.content)