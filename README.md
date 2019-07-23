# RSS Feed Activity Checker - Winslow Mohr
Tool to check whether an RSS feed has had activity in the past X days

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
- An ActivityChecker class containing following functions
  - runActivityChecker
    - input: input_data (either a dictionary or a json file), number of days
    - output: output of activitySince, or None if error
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

# Installation and Run Instructions
## Installation
- Dependencies:
  - Python 3.4+
  - [Pip](https://pip.pypa.io/en/stable/installing/)
- Install required python packages by running:
  - (sudo if necessary) pip install requirements.txt

## Run Instructions
- To run a sample json file, run "python Main.py"
- To run test suite, run "python Main.py test"
- To run with a custom json file (see sample_input.json for format), run "python Main.py <input_json_file>"
- To run with a custom dictionary, please open Main.py and edit test_data and test_num_days on lines 10 and 15, then run "python Main.py dictionary"
- If you would like to log to a file instead of stdout, open Main.py and replace 'stdout' with 'file' on line 7

# Known Problems/Future Work
- Only supports datetime formats of "Fri, 25 Sep 2015 16:27:20 XXXX"
- Compile databse of "frozen" rss feeds to test against
  - Difficult to test output of functions on a moving target of a live RSS feed