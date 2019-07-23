from ActivityChecker import ActivityChecker

class Tester(object):
  def __init__(self, _activity_checker):
    self.ac = _activity_checker
  
  def runAllTests(self):
    self.checkInvalidDayNums()
    self.checkEmptyInput()
    self.checkEmptyValues()
    self.checkOneValuePerKey()
    self.checkMultiValuePerKey()
    self.checkMultipleKeys()
    self.checkInvalidURL()
  
  def checkInvalidDayNums(self): 
    test_data = {
        "bbc": ["http://feeds.bbci.co.uk/news/world/us_and_canada/rss.xml"],
        "bill_maher": ["http://billmaher.hbo.libsynpro.com/rss"],
        "bill_simmons": ["https://rss.art19.com/the-bill-simmons-podcast"]
    } 
    #Negative number of days
    assert self.ac.activitySince(-1,test_data) == None
    #Number of days greater than days since epoch
    assert self.ac.activitySince(800000,test_data) == None
  
  def checkEmptyInput(self):   
    #Empty dictionary
    test_data = {}
    assert self.ac.activitySince(10,test_data) == []
  
  def checkEmptyValues(self):  
    #Key with no values
    test_data = {
        "bbc": ""
    }
    assert self.ac.activitySince(10,test_data) == []
  
  def checkOneValuePerKey(self):   
    #Key with one value
    test_data = {
        "bbc": "http://feeds.bbci.co.uk/news/world/us_and_canada/rss.xml"
    }
    self.ac.activitySince(10,test_data)
  
  def checkMultiValuePerKey(self):  
    #Key with multiple values
    test_data = {
        "bbc": ["http://feeds.bbci.co.uk/news/world/us_and_canada/rss.xml", "http://billmaher.hbo.libsynpro.com/rss"]
    }
    self.ac.activitySince(10,test_data) 
    
  def checkMultipleKeys(self):
    test_data = {
        "bbc": ["http://feeds.bbci.co.uk/news/world/us_and_canada/rss.xml"],
        "bill_maher": ["http://billmaher.hbo.libsynpro.com/rss"],
        "bill_simmons": ["https://rss.art19.com/the-bill-simmons-podcast"]
    }
    
    #Totally valid data and arguments
    self.ac.activitySince(10,test_data)
  
  def checkInvalidURL(self):  
    #Key with invalid URL
    test_data = {
        "bbc": ["http://winslowmo.com/"]
    }
    self.ac.activitySince(10,test_data) 