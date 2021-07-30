#!/usr/bin/python3

from bs4 import BeautifulSoup
from requests import get

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
response = get("https://www.carsales.com.au/cars/?q=(And.Make.Audi._.Year.range(..1985).)", headers=header)

soup = BeautifulSoup(response.text, "html.parser")
model_names = soup.find_all('a', attrs={'data-webm-clickvalue':'sv-title'})

payload = ""
if model_names:
    print("Vehicles found!")
    for model in model_names:
        print(f" - {model.text}")
