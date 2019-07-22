import numpy as np
import requests
import sys
from datetime import datetime, timedelta
from bs4 import BeautifulSoup as bs

from Logger import Logger 

class ActivityChecker(object):
    def __init__(self, _logger):
        self.logger = _logger
    
    def activitySince(self, num_days, company_dict): 
        #Number of days cannot be less than 0
        if(num_days < 0):
            self.logger.logFatalError("Number of days given must be greater than or equal to 0")
            return None
        
        #Number of days cannot go over days since epoch
        try:    
            date_since = datetime.today() - timedelta(days=num_days)  
        except OverflowError:
            self.logger.logFatalError("Invalid number of days provided: " + str(num_days))
            return None
            
        inactive_companies = []

        for company in company_dict:
            rss_feeds = company_dict[company]
            
            #Ensure that the rss feeds are a list, if not, convert to a list
            if not isinstance(rss_feeds,list):
                rss_feeds = [rss_feeds]
                self.logger.logWarning("Converting RSS Feeds for "+ str(company)+" to a list")
            
            #Find latest active date in given RSS feeds
            last_active_date = self.findLastActivity(rss_feeds, company)
            
            #If None is returned, that means somethign went wrong with the parsing
            if(last_active_date == None):
                self.logger.logError("XML parsing for "+ str(company) + " failed")
                continue
            elif(last_active_date < date_since):
                inactive_companies.append(company)
                
            self.logger.logNote("Max date for " + str(company) + ": " + str(last_active_date))
        
        if(len(inactive_companies) == 0):
            self.logger.logNote("No inactive companies found") 
        else:
            self.logger.logNote("List of Inactive Companies: " + str(inactive_companies))   
            
        return inactive_companies
    
    def findLastActivity(self, feeds, company):
        last_active_date = None
        for feed in feeds:
            #Ensure feed URL isn't empty
            if(feed == ''):
                self.logger.logError("Empty RSS feed given for company "+str(company)+" given")
                continue
            
            #Attempt to pull data from the given feed URL
            response = requests.get(feed)
            
            #Ensure request gets a valid response
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
                    #Date format: Fri, 25 Sep 2015 16:27:20 -0000
                    print(pubdate.text)
                    date =  datetime.strptime(pubdate.text, '%a, %d %b %Y %H:%M:%S %z')
                except ValueError:
                    try: 
                        #Date Format: Tue, 18 Jun 2019 00:54:40 GMT
                        date =  datetime.strptime(pubdate.text, '%a, %d %b %Y %H:%M:%S %Z')
                    except ValueError:
                        self.logger.logError("Date value in RSS Feed <"+str(feed)+"> for company "+str(company)+" in unexpected format: " + str(pubdate.text))
                        continue
                
                #Remove timezene info and append to list of dates
                date = date.replace(tzinfo=None)
                pubDates.append(date)
                
            #If there are no pubDates, something went wrong
            if(len(pubDates) > 0):
                #In case the dates are not in sorted order, get the latest date
                maxDate = max(pubDates)
                if(last_active_date == None or maxDate > last_active_date):
                    last_active_date = maxDate
            else:
                self.logger.logError("No dates found at RSS Feed <"+str(feed)+"> for company "+str(company))
        
        return last_active_date   