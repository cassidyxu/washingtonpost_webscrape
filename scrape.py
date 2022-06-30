from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.washingtonpost.com/').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('wp_scrape.csv','w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'timestamp', 'link'])


for article in soup.find_all('div', class_='card'):

    try:
        headline = article.h2.a.span.text
    except Exception as e:
        headline = None
    print(headline)

    try:
        summary = article.find('div', class_='font-size-blurb')
        summary = summary.span.text
    except Exception as e:
        summary = None
    print(summary)

    try:
        timestamp = article.find('span', class_='timestamp').text
    except Exception as e:
        timestamp = None
    print(timestamp)

    try:
        headline_href = article.h2.a['href']
    except Exception as e:
        headline_href = None
    print(headline_href)

    print()

    if not(headline == None and summary == None and timestamp == None and headline_href == None):
        csv_writer.writerow([headline, summary, timestamp, headline_href])

csv_file.close()
