from scraping import log
log_obj=log.Log("Flipkart Requirements").log()

class FlipkartRequirement:

    """This class is created for providing all the
       necessary information to the flipkart page
       like chrome driver executable path,search box class id,
       search button class id etc."""

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
            log_obj.error(str(e))

    def searchitemneeds(self):

        """This function will provides necessary data
           to search item function"""

        try:
            search_bar = '//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input'
            search_button = '//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/button'
            return  search_bar, search_button
        except Exception as e:
            log_obj.error(str(e))

    def loginhandlerneed(self):
        try:
            loginhandler ='_2doB4z' #'_2KpZ6l' #_2doB4z #'/html/body/div[2]/div/div/button'
            return loginhandler
        except Exception as e:
            return log_obj.error(str(e))

    def ratingneed(self):

        """This function will provide data
        to getrating function"""

        try:
            class_name ='_3LWZlK'
            next_btn_class='Next'
            return class_name,next_btn_class
        except Exception as e:
            log_obj.error(str(e))

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
            return e

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
            return log_obj.error(str(e))

    def reviewpageneed(self):

        """This function will provide data
            to reviewpage function"""

        try:
            next_btn_class = 'Next'
            return next_btn_class
        except Exception as e:
            log_obj.error(str(e))

    def productnameneed(self):

        """This function will provide data
        to getproductname page function"""

        try:
            class_name = '_4rR01T'
            next_btn_class = 'Next'
            return class_name,next_btn_class
        except Exception as e:
            log_obj.error(str(e))

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
            log_obj.error(str(e))
