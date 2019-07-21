# Metabolon Tech Assessment - Winslow Mohr
Tech assessment for Metabolon Software Development Engineer

# Requirements
**Given:**
- Dictionary **keyed by Company** and **valued by RSS feed urls**

**Return** 
- Which companies had no activity for a given number of days.

# Assumptions
- The function is passed a dictionary, no input parsing required
  - Parsing functionality will be completed if time allows
- The dictionary is one-key, multiple values
  - If a company has multiple RSS feeds, it will be a list of values for one key
  - Keys are unique
- "Activity" will be defined as last published date

# Design
- An ActivityChecker class containing following functions (planned as of 7/21/2019)
  - activitySince
    - input: number of days, dictionary of companies and RSS feeds
    - output: list of companies with no activity since (current_date) - (number_of_days)
  - findLastActivity
    - input: list of RSS feeds for a specific company
    - output: date of last activity

- A tester class that runs unit tests on AcitivtyChecker class
  - Tests planned as of 7/21/19
    - activitySince
      - Negative number of days
      - Number of days greater than days since epoch (737626 as of 7/21)
      - Empty dictionary
      - Key with no values
      - Key with one value
      - Key with multiple values
    - findLastActivity
      - Empty RSS feed input list
      - One RSS feed
      - Multiple RSS feeds
      - Valid URL
      - Invalid URL