from ActivityChecker import ActivityChecker
from Logger import Logger 
from Tester import Tester

if __name__ == "__main__":
  logger = Logger('stdout')
  checker = ActivityChecker(logger)
  tester = Tester(checker)
  
  tester.checkInvalidDayNums()
  tester.checkEmptyInput()
  tester.checkEmptyValues()
  tester.checkOneValuePerKey()
  tester.checkMultiValuePerKey()
  tester.checkMultipleKeys()
  tester.checkInvalidURL()