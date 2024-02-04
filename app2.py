import requests
from bs4 import BeautifulSoup

class WebCrawler:
    def __init__(self, url):
        # Contructor to initialize the web crawler
        self.url = url
        self.data = [] #List to store the scraped data
        
    def fetch_data(self):
        # Method to send http get request to specified URL and parse the html content
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    
    def parse_data(self, soup):
        # Method to extract relevant data form the parsed HTML 
        table = soup.find('table', {'id': 'hnmain'}) #find the table with id 'hnmain'
        rows = table.find_all('tr', {'class': 'athing',}) #find all rows with class 'athing'
        rows2 = table.find_all('tr') #Find all rows in the table without filtering
        for row in rows2:
            f1 = row.find_next('tr', {'class': 'athing'})
            if f1:
                f2 = f1.find_next('tr')
                data = {} #Create a dictionary to store the extracted data
            
            # Extract data form the html elements
            if f1 and f2: 
                title = f1.find('span', {'class': 'titleline'}).find('a') .text
                order = f1.find('span', {'class': 'rank'}).text
                comments = f2.find_all('a', {'href': lambda href: href and 'item?id=' in href})[-1].text
                points =  f2.find('span', {'class': 'score'})
                points2 = points.text if points else '' 
            
                # Store the extracted data in the dictionary
                data['title'] = title
                data['order'] = order
                data['comments'] = comments
                data['points'] = points2

                # Append the dictionary to the data list
                self.data.append(data)

if __name__ == '__main__':
    # Main block of code to initiate the web crawler, fetch and parse data, and print the results
    crawler = WebCrawler('https://news.ycombinator.com/')
    a = crawler.fetch_data()
    crawler.parse_data(a)

    b = crawler.data #Extract the scraped data from the web crawler isntance

    #Create an empty list to store unique dictionaries from the scraped data
    res_list = [] 
    for i in range(len(b)): #Loop through each item in the original list
        if b[i] not in b[i + 1:]: #Check if the current item is not present in the remaining items of the list
            res_list.append(b[i]) #If it is unique, append it to the result

    for item in res_list:
        print(f"Title: {item['title']}, Order: {item['order']}, Comments: {item['comments']}, Points: {item['points']}")

