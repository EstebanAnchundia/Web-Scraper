# Web-Scraper
Task solution 

Overview:
This Python script is a web scraper designed to extract information from the Hacker News website (https://news.ycombinator.com/). It utilizes the requests library for making HTTP requests and BeautifulSoup for parsing HTML content.

Script Structure:

WebCrawler Class
__init__(self, url)

Constructor method to initialize the web crawler with a specified URL.
Initializes an empty list (self.data) to store scraped data.
fetch_data(self)

Method to send an HTTP GET request to the specified URL and parse the HTML content using BeautifulSoup.
Returns the BeautifulSoup object representing the parsed HTML.
parse_data(self, soup)

Method to extract relevant data from the parsed HTML.
Finds the table with the id 'hnmain' and extracts data from rows with class 'athing'.
Creates dictionaries for each set of extracted data and appends them to the self.data list.

Main Block

Initiates an instance of the WebCrawler class with the Hacker News URL.
Calls fetch_data to get the parsed HTML and parse_data to extract relevant information.
Creates a list res_list to store unique dictionaries from the scraped data.
Eliminates duplicates in the data list and prints the unique items.

To use this script you will need to install the following dependencies:
requests library for making HTTP requests.
BeautifulSoup library for parsing HTML content.

To run it you shall use the following comand:
python app2.py

This version lacks of a method to apply filters and it may not be the most clean solution, but its a creative yet simple design for those who are learning python basics

