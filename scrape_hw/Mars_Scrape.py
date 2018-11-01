


from bs4 import BeautifulSoup as bs
import requests
import pymongo
import pandas as pd
from splinter import Browser


def scrape():


    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')
    print(soup.prettify)





    results = soup.find_all('div', class_ = "slide")
    for result in results:
        title = result.find('div', class_='content_title').text
        news_p = result.find('div', class_='rollover_description_inner').text
        print("____________________")
        print(title)
        print(news_p)





    executable_path = {'executable_path': 'chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    img_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(img_url)
    img_html = browser.html
    img_soup = bs(img_html, 'html.parser')
    img_soup





    #cannot find picture





    tweet_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(tweet_url)
    tweet_html = browser.html
    tweet_soup = bs(tweet_html, 'html.parser')
    tweet_soup
    tweet_result = tweet_soup.find('div', class_='js-tweet-text-container')
    mars_weather = tweet_result.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text
    mars_weather





    mfacts_url = 'https://space-facts.com/mars/'
    tables = pd.read_html(mfacts_url)
    tables





    df_mfacts = tables[0]
    df_mfacts.columns = ['0', '1']
    df_mfacts
    mfacts_html = df_mfacts.to_html
    
    mdict = {"title": title,
             "news_p" : news_p,
             "mars_weather" : mars_weather,
             "mfacts_html" : mfacts_html}
    return mdict 

