from bs4 import BeautifulSoup
import requests
import csv

#function for getting only text from the tag or getting 'unknown' if empty tag is given
def get_text_or_unknown(tag):
    return tag.text.strip() if tag else "unknown"

def Job_Listing_Scraper():

    #url of site we are working on
    url = 'https://realpython.github.io/fake-jobs/'
    #getting the text we can work on by requests 'get' method
    result = requests.get(url)
    #transforming the text into BeautifulSoup object
    doc = BeautifulSoup(result.text, "html.parser")

    #finding tags containing data we need
    body = doc.body
    container = body.find(id='ResultsContainer')
    joblistings = container.find_all('div', class_='column is-half')

    with open("joblistings.csv", 'w', newline='') as f:

        writer = csv.writer(f)
        writer.writerow(['title', 'company-name', 'location', 'detail-page-url'])
        
        #iterating through the tag that contains data
        for job in joblistings:

            #using function to get all data ready for csv file
            title = get_text_or_unknown(job.find('h2'))
            company = get_text_or_unknown(job.find('h3'))
            location = get_text_or_unknown(job.find('p'))

            #using 'get' to get the url we want to use
            job_detail = job.find('a', string='Apply')
            apply_url = job_detail.get('href')

            writer.writerow([title, company, location, apply_url])



if __name__ == "__main__":
    Job_Listing_Scraper()

