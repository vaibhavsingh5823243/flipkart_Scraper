from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd
import time
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
#chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
import logging as lg
class Log:

    def __init__(self,name):
        self.name=name

    def log(self):

        logger=lg.getLogger(self.name)
        logger.setLevel(lg.DEBUG)
        format=lg.Formatter("%(asctime)s:%(name)s:(levelname)s:%(message)s")
        filehandler=lg.FileHandler("test.log")
        filehandler.setFormatter(format)
        logger.addHandler(filehandler)
        return logger

class FlipkartRequirement:

    """This class is created for providing all the
           necessary information to the flipkart page
           like chrome driver executable path,search box class id,
           search button class id etc."""

    def __init__(self):
        self.log_writer = Log('FlipkartRequirement').log()


    def flipkartpageneeds(self):

        """This function will provide data
           to flipkart page function"""

        try:
            google_link = 'https:\\www.google.com'
            search_box='q'
            search_btn='btnK'
            website_name = 'flipkart'
            website_url_xpath = '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div[1]/a/h3'
            return google_link,search_box,search_btn,website_name, website_url_xpath

        except Exception as e:
            self.log_writer.error(str(e))

    def searchitemneeds(self):

        """This function will provides necessary data
           to search item function"""

        try:
            search_bar = '//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input'
            search_button = '//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/button'
            return  search_bar, search_button
        except Exception as e:
            self.log_writer.error(str(e))

    def loginhandlerneed(self):

        try:
            loginhandler ='_2doB4z' #'_2KpZ6l' #_2doB4z #'/html/body/div[2]/div/div/button'
            return loginhandler

        except Exception as e:
            return self.log_writer.error(str(e))

    def ratingneed(self):

        """This function will provide data
        to getrating function"""

        try:
            class_name ='_3LWZlK'
            next_btn_class='Next'
            return class_name,next_btn_class
        except Exception as e:
            self.log_writer.error(str(e))

    def priceneed(self):

        """This function will provide data
        to getprice function"""

        try:
            pattern = "^₹[0-9]+,+[[0-9]+,?]*[0-9]+"
            price_class1 = '_30jeq3'
            price_class2 = '_1_WHN1'
            next_btn_class='Next'
            return price_class1, price_class2,next_btn_class
        except Exception as e:
            return self.log_writer.error(str(e))


    def priceandratingneed(self):

        """This function will provide data
            to priceandrating function"""

        try:
            class_rating = '_3LWZlK'
            pattern = "^₹[0-9]+,+[[0-9]+,?]*[0-9]+"
            class_num1 = '_30jeq3'#_3tbKJL'
            class_num2 = '_1_WHN1'#'_25b18c'
            class_name = '_4rR01T'
            next_btn_class = 'Next'

            return class_rating, pattern, class_num1, class_num2,class_name,next_btn_class
        except Exception as e:
            return self.log_writer.error(str(e))

    def reviewpageneed(self):

        """This function will provide data
            to reviewpage function"""

        try:
            next_btn_class = 'Next'
            return next_btn_class
        except Exception as e:
            self.log_writer.error(str(e))

    def productnameneed(self):

        """This function will provide data
        to getproductname page function"""

        try:
            class_name = '_4rR01T'
            next_btn_class = 'Next'
            return class_name,next_btn_class
        except Exception as e:
            self.log_writer.error(str(e))

    def reviewsneed(self):

        """This function will provide data
        to getreview function"""
        try:

            more_review_1 = "_3UAT2v"#_3at_-o"
            more_review_2 = "_33R3aa"#_3UAT2v"
            heading_class = '_2-N8zT'
            review_class = 't-ZTKy'
            next_btn_class = 'Next'
            name_class='_2V5EHH'
            rating_class=['_3LWZlK',"_1BLPMq"]
            return more_review_1, more_review_2,name_class,rating_class,heading_class,review_class,next_btn_class
        except Exception as e:
            self.log_writer.error(str(e))

data_obj=FlipkartRequirement()

class Flipkart:

    def __init__(self):
        self.driver = webdriver.Chrome("D:\\DjangoProject\\flipkart_scraper\\chromedriver_win32\\chromedriver.exe", options=chrome_options)
        self.log_writer = Log('Flipkart').log()

    def getFlipkartPage(self):

        """It will redirect  to flipkart website official page"""

        try:
            google_link, search_box, search_btn, website_name, website_url_xpath = data_obj.flipkartpageneeds()
            self.driver.get(google_link)
            self.log_writer.info("Google chrome opened.")
            time.sleep(1)
            self.driver.find_element_by_name(search_box).send_keys(website_name)
            time.sleep(1)
            self.driver.find_element_by_name(search_btn).send_keys(Keys.ENTER)
            time.sleep(1)
            self.driver.find_element_by_xpath(website_url_xpath).click()
            self.log_writer.info("Flipkart Url hits")

        except Exception as e:
            self.log_writer.error(str(e))

    def searchItem(self, search_item):

        """This function will return the search result of flipkart search bar"""

        try:
            search_bar, search_button = data_obj.searchitemneeds()
            self.driver.find_element_by_xpath(search_bar).send_keys(search_item)
            self.driver.find_element_by_xpath(search_button).click()
            self.log_writer.info("Searching for all possible result...")
        except Exception as e:
            self.log_writer.error(str(e))

    def isPresent(self, value):

        """This function will return True if particular
        code(class_name,xpath,css selector,link text etc)
        present in the page source else it will return False."""

        try:
            if self.driver.page_source.find(value) != -1:
                return True
            else:
                return False
        except Exception as e:
            self.log_writer.error(str(e))


    def getLoginPopHandler(self):

        """This function will remove the
        login popup from Flipkart site"""

        try:
            loginhandler = data_obj.loginhandlerneed()
            self.driver.find_element_by_class_name(loginhandler).click()
            self.log_writer.info("Login popups removed.")

        except Exception as e:
            self.log_writer.error(str(e))

    def function(self, item):

        """This function will call all the initial function
           like create chrome page ,creating Flipkart Page."""

        try:
            self.getFlipkartPage()
            self.getLoginPopHandler()
            self.searchItem(item)
            self.log_writer.info("All function called successfully.")

        except Exception as e:
            self.log_writer.error(str(e))

    def getAllUrl(self):

        """This function will return the url of
        all products that belongs to that page"""

        try:
            product_links = []
            # page_links = []
            time.sleep(1)
            linksobj = self.driver.find_elements_by_tag_name('a')
            for obj in linksobj:
                link = obj.get_attribute('href')
                if '?pid' in link:
                    product_links.append(link)
                # elif 'off&as=off&page' in link:
                # page_links.append(link)
            self.log_writer.info("List of products links created.")
            return product_links

        except Exception as e:
            self.log_writer.error(str(e))

    def getPrice(self, num):

        """This function will return the list
         of prices in proper formats"""

        try:
            price_class1, price_class2, next_btn_class = data_obj.priceneed()

            prices = [['Price']]
            while True:
                time.sleep(2)
                if self.isPresent(price_class1):
                    priceobj = self.driver.find_elements_by_class_name(price_class1)
                elif self.isPresent(price_class2):
                    priceobj = self.driver.find_elements_by_class_name(price_class2)
                for obj in priceobj:
                    prices.append([int(obj.text.replace(",", "")[1:])])
                if self.isPresent(next_btn_class) != True or len(prices) >= num:
                    break
                elif self.isPresent(next_btn_class):
                    time.sleep(3)
                    self.driver.find_element_by_link_text(next_btn_class.upper()).click()
            return prices
        except Exception as e:
            self.log_writer.error(e)
            return prices

    def getProductName(self, num):

        """This function will return the
         list of names of all products."""

        try:
            class_name, next_btn_class = data_obj.productnameneed()
            products_name = []
            while True:
                time.sleep(1)
                if self.isPresent(class_name):
                    name_obj = self.driver.find_elements_by_class_name(class_name)
                    for name in name_obj:
                        products_name.append(name.text)
                    if self.isPresent(next_btn_class) != True or len(products_name) >= num:
                        self.log_writer.error("Next button does't exist.")
                        break
                    elif self.isPresent(next_btn_class):
                        time.sleep(2)
                        self.driver.find_element_by_link_text(next_btn_class.upper()).click()

            self.log_writer.info("List of Names of all products created.")
            return products_name

        except Exception as e:
            self.log_writer.error(str(e))

    def getRating(self, num):

        """This function will return the
        list of rating of all products"""

        try:
            rating_class, next_btn_class = data_obj.ratingneed()
            ratings = [['Ratings']]
            while True:
                time.sleep(2)
                if self.isPresent(rating_class):
                    rating_obj = self.driver.find_elements_by_class_name(rating_class)
                for obj in rating_obj:
                    ratings.append([float(obj.text)])
                if self.isPresent(next_btn_class) != True or len(ratings) >= num:
                    break
                elif self.isPresent(next_btn_class):
                    time.sleep(3)
                    self.driver.find_element_by_link_text(next_btn_class.upper()).click()
            return ratings

        except Exception as e:
            self.log_writer.error(e)
            return ratings

    def getRatingsAndPrices(self, num):

        """This function will return the lists of name,
           rating and price of all products."""

        try:
            class_rating, pattern, class_price1, class_price2, class_name, next_btn_class = data_obj.priceandratingneed()
            data=[["Names","Prices","Ratings"]]
            while True:

                condition1 = (self.isPresent(class_rating) and self.isPresent(class_price1)) and self.isPresent(
                    class_name)
                condition2 = (self.isPresent(class_rating) and self.isPresent(class_price2)) and self.isPresent(
                    class_name)
                if condition1 or condition2:
                    time.sleep(1)
                    rating_obj = self.driver.find_elements_by_class_name(class_rating)
                    time.sleep(1)
                    name_obj = self.driver.find_elements_by_class_name(class_name)
                    time.sleep(1)
                    if self.isPresent(class_price1):
                        price_obj = self.driver.find_elements_by_class_name(class_price1)
                    elif self.isPresent(class_price2):
                        price_obj = self.driver.find_elements_by_class_name(class_price2)
                    for rating, price, name in zip(rating_obj, price_obj, name_obj):
                        l=[name.text[:35],int(price.text.replace(",", "")[1:]),float(rating.text)]
                        data.append(l)
                    if len(data) >= int(num) or self.isPresent(next_btn_class) != True:
                        self.log_writer.error("Next Button does't exist.")
                        break
                    elif self.isPresent(next_btn_class):
                        WebDriverWait(self.driver, 30).until(
                            EC.presence_of_element_located((By.LINK_TEXT, next_btn_class.upper())))
                        self.driver.find_element_by_link_text(next_btn_class.upper()).click()
            self.log_writer.info("List of names,prices and ratings of all products created.")
            return data
        except Exception as e:
            self.log_writer.error(str(e))

    def reviews(self, no_of_reviews):
        try:
            more_class1, more_class2, reviewer_class, rating_class, heading_class, review_class, next_btn_class = data_obj.reviewsneed()
            data=[['Reviewer','Ratings','Heading','Review']]
            while True:
                current_url = self.driver.current_url
                time.sleep(2)
                product_links = self.getAllUrl()
                inside_break = False
                for link in product_links:
                    time.sleep(1)
                    self.driver.get(link)
                    time.sleep(1)
                    if self.isPresent(more_class1):
                        self.driver.find_element_by_class_name(more_class1).click()
                    elif self.isPresent(more_class2):
                        self.driver.find_element_by_class_name(more_class2).click()
                    time.sleep(3)
                    self.driver.find_element_by_link_text(next_btn_class.upper()).click()
                    while True:
                        condition1 = self.isPresent(reviewer_class) and self.isPresent(rating_class[0])
                        condition2 = self.isPresent(heading_class) and self.isPresent(review_class)
                        if condition1 and condition2:
                            time.sleep(2)
                            reviewer_obj = self.driver.find_elements_by_class_name(reviewer_class)
                            rating_obj = self.driver.find_elements_by_class_name(rating_class[0])
                            heading_obj = self.driver.find_elements_by_class_name(heading_class)
                            review_obj = self.driver.find_elements_by_class_name(review_class)
                            for name, rating, heading, review in zip(reviewer_obj, rating_obj, heading_obj, review_obj):
                                d=[name.text,rating.text,heading.text,review.text]
                                data.append(d)
                            if len(data) >= no_of_reviews:
                                inside_break = True
                                break
                            elif self.isPresent(next_btn_class) == True:
                                WebDriverWait(self.driver, 30).until(
                                    EC.presence_of_element_located((By.LINK_TEXT, next_btn_class.upper())))
                                self.driver.find_element_by_link_text(next_btn_class.upper()).click()
                            else:
                                break
                    if inside_break:
                        break
                self.driver.get(current_url)
                if inside_break or self.isPresent(next_btn_class) == False:
                    break
                else:
                    WebDriverWait(self.driver, 30).until(
                        EC.presence_of_element_located((By.LINK_TEXT, next_btn_class.upper())))
                    self.driver.find_element_by_link_text(next_btn_class.upper()).click()
            return data

        except Exception as e:
            self.log_writer.error(e)

class Searching:

    def __init__(self,search,category,number):
        self.search = search
        self.category = category
        self.number = int(number)
        self.log_writer =  Log('Searching').log()

    def getdata(self):
        try:
            obj=Flipkart()
            obj.function(self.search)
            if self.category == 'price':
                data = obj.getPrice(self.number)
            elif self.category == 'rating':
                data = obj.getRating(self.number)
            elif self.category == 'review':
                data = obj.reviews(self.number)
            else:
                data = obj.getRatingsAndPrices(self.number)
            return data

        except Exception as e:
            self.log_writer.error(str(e))

    def too_csv(self):
        try:
            filename=self.search.lower()+self.category.lower()+'.csv'
            path="scraper\\static\\scraper\\files\\"+filename
            data=self.getdata()
            data_csv=pd.DataFrame(data[1:],columns=data[0])
            data_csv.to_csv(path)

            return data,filename

        except Exception as e:
            self.log_writer.error(str(e))
