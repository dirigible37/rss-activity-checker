import numpy as np
import requests
from datetime import datetime, timedelta
from bs4 import BeautifulSoup as bs


class ActivityChecker(object):
    
    def activitySince(self, num_days, company_dict):
        assert num_days > 0
        date_since = datetime.today() - timedelta(days=num_days)
        
        inactive_companies = []

        for company in company_dict:
            rss_feeds = company_dict[company]
            last_active_date = self.findLastActivity(rss_feeds)
            if(last_active_date == None):
                print("XML parsing failed")
            elif(last_active_date < date_since):
                inactive_companies.append(company)
        
        return inactive_companies

    def findLastActivity(self, feeds):
        last_active_date = None
        for feed in feeds:
            response = requests.get(feed).text
            soup = bs(response,'xml')
            for pubdate in soup.find_all('pubDate'):
                print(pubdate.text)
        
        return last_active_date

test_data = {
    "bill_maher": ["http://billmaher.hbo.libsynpro.com/rss"],
    "bill_simmons": ["https://rss.art19.com/the-bill-simmons-podcast"]
}
checker = ActivityChecker()
inactive = checker.activitySince(10, test_data)