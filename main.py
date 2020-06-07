from src.site.TowardsDataScienceScrap import TowardsDataScienceScrap

def scrape(url):
    scrap = TowardsDataScienceScrap(url)
    return scrap.save_post_details()

site_urls = [
    'https://towardsdatascience.com/data-science/home',
    'https://towardsdatascience.com/machine-learning/home',
    'https://towardsdatascience.com/programming/home',
    'https://towardsdatascience.com/data-visualization/home',
    'https://towardsdatascience.com/artificial-intelligence/home',
    'https://towardsdatascience.com/video/home',
    'https://towardsdatascience.com/'
]

if __name__ == '__main__':
    print("\n Begin Web Scrapping")
    data = list(map(scrape, site_urls))
    print("\n Scrapping Results: ")
    for d in data:
        print(d)