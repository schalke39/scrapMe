from src.scrapper.BaseScrapper import BaseScrapper
from bs4 import BeautifulSoup
import pandas as pd
import os
from datetime import datetime

class TowardsDataScienceScrap(BaseScrapper):

    """
        Post Details
            -post id
            -post image
            -post url
            -post title
            -post-summary
            -post author avtar
            -post author page url
            -post author id
            -post author name
            -post datetime
            -post read time
    """

    def __init__(self,url):
        self.driver = self.get_driver(url)
        self.source = self.scroll_to_bottom_of_page(
            self.driver).page_source
        self.soup = BeautifulSoup(self.source,'html5lib')
        self.site_url = url
        super().__init__(self.site_url, self.soup)
        self.driver.quit()

    def find_all_post(self):
        return [post for post in self.soup.find_all('div')
                if post.has_attr('data-post-id')]

    def get_post_image(self,post):
        # Working fine
        find_image_link = post.contents[0].find('a')
        if find_image_link is not None:
            return self.get_background_image(find_image_link)
        else:
            return None

    def get_post_url(self,post):
        # Working fine
        find_post_link = post.contents[0].find('a')
        if find_post_link is not None:
            return find_post_link['href']
        else:
            return None

    def get_post_title(self,post):
        # Working Fine
        find_post_title = post.find('h3')
        if find_post_title is not None:
            return find_post_title.div.text
        else:
            return None

    def get_post_summary(self,post):
        # Working fine
        if len(post.contents) == 2:
            find_summary = post.contents[1].find('a',recursive=False).find('div',recursive=False)
            if find_summary is not None and find_summary.string is not None:
                return find_summary.string
            else:
                find_summary = post.contents[1].contents[1].contents[1].div.string
                if find_summary is not None and find_summary.string is not None:
                    return find_summary.string
                else:
                    return None
        else:
            find_summary = post.div.a.find('div',recursive=False)
            if find_summary is not None and find_summary.string is not None:
                return find_summary.string
            else:
                find_summary = post.div.find("div",recursive=False).div.a.find('div',recursive=False)
                if find_summary is not None and find_summary.string is not None:
                    return find_summary.string
                else:
                    return None

    def get_post_author_avatar(self,post):
        if len(post.contents) == 2:
            find_author_avatar = post.contents[1].find('div',recursive=False).find('div',recursive=False).find('img')
            if find_author_avatar is not None:
                return find_author_avatar['src']
            else:
                return None
        else:
            find_author_avatar = post.contents[0].find('div',recursive=False).find('div',recursive=False).\
                find("div",recursive=False).div.div.find("img")
            if find_author_avatar is not None:
                return find_author_avatar['src']
            else:
                return None

    def get_post_author_page_url(self,post):
        if len(post.contents) == 2:
            find_author_page = post.contents[1].find('div',recursive=False).find('div',recursive=False).\
                find('div',recursive=False).find('a')
            if find_author_page is not None and find_author_page['href'] is not None:
                return find_author_page['href']
            else:
                return None
        else:
            find_author_page = post.contents[0].find('div',recursive=False).find('div',recursive=False).\
                find("div",recursive=False).div.div.find('a')
            if find_author_page is not None and find_author_page['href'] is not None:
                return find_author_page['href']
            else:
                return None

    def get_post_author_id(self,post):
        if len(post.contents) == 2:
            find_author_page = post.contents[1].find('div',recursive=False).find('div',recursive=False).\
                find('div',recursive=False).find('a')
            if find_author_page is not None and find_author_page['data-user-id'] is not None:
                return find_author_page['data-user-id']
            else:
                return None
        else:
            find_author_page = post.contents[0].find('div',recursive=False).find('div',recursive=False).\
                find("div",recursive=False).div.div.find('a')
            if find_author_page is not None and find_author_page['data-user-id'] is not None:
                return find_author_page['data-user-id']
            else:
                return None

    def get_post_author_name(self,post):
        if len(post.contents) == 2:
            find_author_name = post.contents[1].find('div',recursive=False).find('div',recursive=False).contents[1].a
            if find_author_name is not None and find_author_name.text is not None:
                return find_author_name.text
            else:
                return None
        else:
            find_author_name = post.contents[0].find('div',recursive=False).find('div',recursive=False).contents[1].a
            if find_author_name is not None and find_author_name.text != '':
                return find_author_name.text
            else:
                find_author_name = post.contents[0].find('div',recursive=False).div.contents[1].div.contents[1].a
                if find_author_name is not None and find_author_name.text != '':
                    return find_author_name.text
                else:
                    return None

    def get_post_time(self,post):
        if len(post.contents) == 2:
            find_post_time = post.contents[1].find('div',recursive=False).find('div',recursive=False).\
            contents[1].find('time')
            if find_post_time is not None and find_post_time['datetime'] is not None:
                return find_post_time['datetime']
            else:
                return None
        else:
            find_post_time = post.contents[0].find('div',recursive=False).div.contents[1].find('time')
            if find_post_time is not None and find_post_time['datetime'] is not None:
                return find_post_time['datetime']
            else:
                return None

    def get_post_read_time(self,post):
        if len(post.contents) == 2:
            find_post_read_time = post.contents[1].find('div',recursive=False).find('div',recursive=False).\
            contents[1].find('span',title=True)
            if find_post_read_time is not None:
                return find_post_read_time['title']
            else:
                return None
        else:
            find_post_read_time = post.contents[0].find('div',recursive=False).find('span',{'class':'readingTime'})
            if find_post_read_time is not None and find_post_read_time['title'] is not None:
                return find_post_read_time['title']
            else:
                return None

    def get_post(self,url):
        pass

    def get_post_details(self,post):

        post_details = {'post_id': post['data-post-id'],'post_title': self.get_post_title(post),
                        'post_summary': self.get_post_summary(post),
                        'post_author_page_url': self.get_post_author_page_url(post),
                        'post_author_id': self.get_post_author_id(post),
                        'post_author_name': self.get_post_author_name(post),
                        'post_datetime': self.get_post_time(post),
                        'post_read_time': self.get_post_read_time(post)
                        }

        return post_details

    def get_all_post_details(self):
        return list(map(self.get_post_details,self.find_all_post()))

    def save_post_details(self):
        try:
            for root, dirs, files in os.walk(os.environ['PYTHONPATH']+'\\others'):
                if not 'post_'+datetime.now().strftime('%Y%m%d') in files:
                    post_data = self.get_all_post_details()
                    df = pd.DataFrame(post_data)
                    print('Path: '+ os.path.abspath('.')+'\\others\\post_'+datetime.now().strftime('%Y%m%d')+'.csv')
                    df.to_csv(os.environ['PYTHONPATH']+'\\others\\post_'+datetime.now().strftime('%Y%m%d')+'.csv',header=True,index=False)
                else:
                    print('File already generated')
        except Exception as e:
            print(e)

s_url = "https://towardsdatascience.com/data-science/home"
obj = TowardsDataScienceScrap(s_url)
obj.save_post_details()