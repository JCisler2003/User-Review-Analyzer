import requests 
from bs4 import BeautifulSoup
from selenium import webdriver


#Opens a file in folder called 'reviews.txt'. If there is no file, it automatically creates it
open('4090.txt', 'w')
open('4080.txt', 'w')
open('4070.txt', 'w')
open('4060.txt', 'w')


#Opens the text file containing the URLs
with open('URL.txt', 'r') as textFile:

    #Uses Selenium to open up a Chrome tab. Since the page dynamically loads, we need this to open everything up to start scraping
    driver = webdriver.Chrome()

    #grabs the first line URL.txt.
    url = textFile.readline()

    #gets url for selenium to load the page
    driver.get(url)

    html = driver.page_source


    #Use beautiful soup to prepare the html parser
    soup = BeautifulSoup(html, 'html.parser')

    
    #I had an issue where the Amazon bot detection service forced me to sign in to see the reviews.
    #This loop keeps opening new chrome tabs until I am not at the sign in page
    while soup.find('div', class_='a-row a-spacing-small review-data') == None:
        driver = webdriver.Chrome()

        driver.get(url)

        html = driver.page_source

        soup = BeautifulSoup(html, 'html.parser')




    

    #Loops until a blank line of URL.txt
    while url != '\n':

        
        
        driver.get(url)

        html = driver.page_source


        #Use beautiful soup to prepare the html parser
        soup = BeautifulSoup(html, 'html.parser')

        #Finds all instances of a div with that specific class and puts them into an array
        reviews = soup.find_all('div', class_='a-row a-spacing-small review-data')

        #Loops until the end of the array of reviews
        for indReview in reviews:
            
            
            #Writes each review into a seperate text file. We need 'encoding = 'utf-8'' because of the copyright symbols. 
            with open('4090.txt', 'a', encoding = 'utf-8') as review:
                        review.write(indReview.get_text(strip = True))
                        review.write("\n")




        url = textFile.readline()





    url = textFile.readline()

    #Loops until a blank line of URL.txt
    while url != '\n':

        
        
        driver.get(url)

        html = driver.page_source


        #Use beautiful soup to prepare the html parser
        soup = BeautifulSoup(html, 'html.parser')

        #Finds all instances of a div with that specific class and puts them into an array
        reviews = soup.find_all('div', class_='a-row a-spacing-small review-data')

        #Loops until the end of the array of reviews
        for indReview in reviews:
            
            
            #Writes each review into a seperate text file. We need 'encoding = 'utf-8'' because of the copyright symbols. 
            with open('4080.txt', 'a', encoding = 'utf-8') as review:
                        review.write(indReview.get_text(strip = True))
                        review.write("\n")



        url = textFile.readline()

    url = textFile.readline()


    while url != '\n':

        
        
        driver.get(url)

        html = driver.page_source


        #Use beautiful soup to prepare the html parser
        soup = BeautifulSoup(html, 'html.parser')

        #Finds all instances of a div with that specific class and puts them into an array
        reviews = soup.find_all('div', class_='a-row a-spacing-small review-data')

        #Loops until the end of the array of reviews
        for indReview in reviews:
            
            
            #Writes each review into a seperate text file. We need 'encoding = 'utf-8'' because of the copyright symbols. 
            with open('4070.txt', 'a', encoding = 'utf-8') as review:
                        review.write(indReview.get_text(strip = True))
                        review.write("\n")



        url = textFile.readline()


    url = textFile.readline()


    while url != '\n':

        
        
        driver.get(url)

        html = driver.page_source


        #Use beautiful soup to prepare the html parser
        soup = BeautifulSoup(html, 'html.parser')

        #Finds all instances of a div with that specific class and puts them into an array
        reviews = soup.find_all('div', class_='a-row a-spacing-small review-data')

        #Loops until the end of the array of reviews
        for indReview in reviews:
            
            
            #Writes each review into a seperate text file. We need 'encoding = 'utf-8'' because of the copyright symbols. 
            with open('4060.txt', 'a', encoding = 'utf-8') as review:
                        review.write(indReview.get_text(strip = True))
                        review.write("\n")



        url = textFile.readline()
        