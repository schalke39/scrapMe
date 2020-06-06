from dump.TowardsDataScienceScrap import TowardsDataScienceScrap

def scrape(url):
    scrap = TowardsDataScienceScrap(url)
    scrap.save_post_details()

site_urls = [
    'https://towardsdatascience.com/data-science/home',
    'https://towardsdatascience.com/machine-learning/home',
    'https://towardsdatascience.com/programming/home',
    'https://towardsdatascience.com/data-visualization/home',
    'https://towardsdatascience.com/artificial-intelligence/home',
    'https://towardsdatascience.com/video/home'
]

# important - https://medium.com/python-pandemonium/6-things-to-develop-an-efficient-web-scraper-in-python-1dffa688793c

# https://towardsdatascience.com/data-science/home
# https://www.reddit.com/r/learnpython/comments/3wzgse/python_beautifulsoup_question_is_there_a_way_to/
# https://www.freecodecamp.org/news/better-web-scraping-in-python-with-selenium-beautiful-soup-and-pandas-d6390592e251/
# https://stackoverflow.com/questions/5015483/test-if-an-attribute-is-present-in-a-tag-in-beautifulsoup
# https://medium.com/datadriveninvestor/speed-up-web-scraping-using-multiprocessing-in-python-af434ff310c5
# https://stackoverflow.com/questions/24981963/extracting-url-from-style-background-url-with-beautifulsoup-and-without-regex
# https://stackoverflow.com/questions/36108621/get-all-html-tags-with-beautiful-soup
# https://www.youtube.com/watch?v=ng2o98k983k
# https://www.pluralsight.com/guides/advanced-web-scraping-tactics-python-playbook
# https://www.quora.com/How-do-I-crawl-a-website-that-loads-content-lazily
# https://www.tidbitsofprogramming.com/2014/02/crawling-website-that-loads-content.html
# https://www.scraperapi.com/documentation


# https://www.tidbitsofprogramming.com/2014/02/crawling-website-that-loads-content.html
# https://www.quora.com/How-do-I-crawl-a-website-that-loads-content-lazily

# //*[@data-index]