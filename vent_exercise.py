import arrow
from flashtext import KeywordProcessor
import pandas as pd

# using arrow to get the current time in EST in the given format
utc = arrow.utcnow()
local = utc.to('US/Eastern')
print("It is currently: " + local.format('MM-DD-YY HH:mm:ss'))

# using pandas to print out a formatted excel sheet
ex = pd.read_excel('venv_example.xlsx', index_col='Test')
print(ex)

# using flashtext to find keywords in a string
word_string = "Word1 is all about word2 but it is all out so there are no more words."
keyword_processor = KeywordProcessor()
keyword_processor.add_keyword('Word1')
keyword_processor.add_keyword('Word2')
keyword_processor.add_keyword('No More Words')
print("Keywords found: " + str(keyword_processor.extract_keywords(word_string)))
