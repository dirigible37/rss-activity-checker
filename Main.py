import sys
from ActivityChecker import ActivityChecker
from Logger import Logger 
from Tester import Tester

if __name__ == "__main__":
  logger = Logger('stdout')
  checker = ActivityChecker(logger)

  test_data = {
    "bbc": ["http://feeds.bbci.co.uk/news/world/us_and_canada/rss.xml"],
    "bill_maher": ["http://billmaher.hbo.libsynpro.com/rss"],
    "bill_simmons": ["https://rss.art19.com/the-bill-simmons-podcast"]
  }
  test_num_days = 10
  
  if(len(sys.argv) == 1):
    logger.logNote("No input file provided, processing sample_input.json")
    input_file = "sample_input.json"
    checker.runActivityChecker(input_data=input_file)
  elif(len(sys.argv) == 2):
    input_file = sys.argv[1]
    #Run the test suite
    if(input_file == "test"):
      tester = Tester(checker)
      tester.runAllTests()
    #Run a dictionary input
    elif(input_file == "dictionary"):
      checker.runActivityChecker(input_data=test_data, num_days=test_num_days)
    #Run file input
    else: 
      logger.logNote("Input file provided: " + input_file)
      checker.runActivityChecker(input_data=input_file)
  else:
    logger.logFatalError("Invalid arguments. Run with: 'python Main.py <input_json_file>'")
  
