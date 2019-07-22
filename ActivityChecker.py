import numpy as np
import requests
import sys
from datetime import datetime, timedelta
from bs4 import BeautifulSoup as bs

from Logger import Logger 

class ActivityChecker(object):
    def __init__(self):
        self.logger = Logger('file')
    
    def activitySince(self, num_days, company_dict):
        if(num_days < 0):
            self.logger.logFatalError("Number of days given must be greater than or equal to 0")
            sys.exit()
            
        date_since = datetime.today() - timedelta(days=num_days)  
        inactive_companies = []

        for company in company_dict:
            rss_feeds = company_dict[company]
            
            #Ensure that the rss feeds are a list, if not, convert to a list
            if not isinstance(rss_feeds,list):
                rss_feeds = [rss_feeds]
                self.logger.logWarning("RSS Feeds for company should be a list")
            
            last_active_date = self.findLastActivity(rss_feeds, company)
            
            #If None is returned, that means somethign went wrong with the parsing
            if(last_active_date == None):
                self.logger.logError("XML parsing for "+ str(company) + " failed")
                continue
            elif(last_active_date < date_since):
                inactive_companies.append(company)
                
            self.logger.logNote("Max date for " + str(company) + ": " + str(last_active_date))
            
        self.logger.logNote("List of Inactive Companies:")
        self.logger.logNote(inactive_companies)    
        return inactive_companies
    
    def findLastActivity(self, feeds, company):
        last_active_date = None
        for feed in feeds:
            #Attempt to pull data from the given feed URL
            response = requests.get(feed)
            if(response.status_code != 200):
                self.logger.logError("RSS Feed <"+str(feed)+"> for company "+str(company)+" not accessible")
                continue
            res_text = response.text
            
            #Use BeautifulSoup to parse XML
            soup = bs(res_text,'xml')
            pubDates = []
            
            #Loop through all instances of "pubDate" in given XML
            for pubdate in soup.find_all('pubDate'):
                try:
                    date =  datetime.strptime(pubdate.text, '%a, %d %b %Y %H:%M:%S %z')
                except ValueError:
                    try: 
                        date =  datetime.strptime(pubdate.text, '%a, %d %b %Y %H:%M:%S %Z')
                    except ValueError:
                        self.logger.logError("Date value in RSS Feed <"+str(feed)+"> for company "+str(company)+" in unexpected format: " + str(pubdate.text))
                        continue
                
                date = date.replace(tzinfo=None)
                pubDates.append(date)
                
            #If there are no pubDates, something went wrong
            if(len(pubDates) > 0):
                #In case the dates are not in sorted order, get the latest date
                maxDate = max(pubDates)
                if(last_active_date == None):
                    last_active_date = maxDate
                elif(maxDate > last_active_date ):
                    last_active_date = maxDate
            else:
                self.logger.logError("No dates found at RSS Feed <"+str(feed)+"> for company "+str(company))
        
        return last_active_date

if __name__ == "__main__":
    test_data = {
        "bbc": ["http://feeds.bbci.o.uk/news/world/us_and_canada/rss.xml"],
        "bill_maher": ["http://billmaher.hbo.libsynpro.com/rss"],
        "bill_simmons": ["https://rss.art19.com/the-bill-simmons-podcast"]
    }
    checker = ActivityChecker()
    inactive = checker.activitySince(10, test_data)
    