import requests, bs4

weather_url = "https://weather.com/weather/tenday/l/Erie+PA?canonicalCityId=e7790299f9f059a7ecd41d21209994c14d0256713d41822244be372885cbe753"
req = requests.get(weather_url)
req.raise_for_status()

weather_soup = bs4.BeautifulSoup(req.text, 'html.parser')

temp = weather_soup.select(".DailyContent--temp--1s3a7")[0].text
weather = weather_soup.select("#detailIndex0 > div > div:nth-child(1) > p")[0].text

weather.split()

print("Current Weather for Erie, PA")
print("Temperature: ", temp)
print(weather)
input("> ")

import newsapi

with open("api_key.txt") as file:
    api_key = file.read()

newsclient = newsapi.NewsApiClient(api_key=api_key)
articles = newsclient.get_top_headlines(sources="bbc-news")['articles']

for i in range(10):
    print(articles[i]['title'])

input("> ")