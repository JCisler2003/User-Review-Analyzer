# CS-325-Project-Web Scraper

Created by Joseph Cisler

# Description
This program uses beautiful soup and Selenium to scrape user reviews from Amazon. The program grabs URLs from the "URL.txt" text file and scrapes the user reviews for each URL. After the reviews are scraped, they are placed in designated output files for each product URL. The example used for this project was the Nvidia 40 series graphics cards.

# Details
a requirements.yaml file is provided to have the correct packages and environment for the program. To change what you are scraping for, simply provide the URL to an Amazon product in the URL.txt file. The program scrapes up to four different products at a time by putting a blank line between the URLs in the URL.txt file. If less thatn four URLs are being scraped, remove
while loops as needed. You can also change what the output files are called by changing the names of the files near the top of the program.
