## This code generates partisan word clouds surrounding a specific phrase.  That is, it takes as an input argument a phrase,
## and date range, and returns two word clouds showing words commonly used by Republicans and words commonly 
## used by Democrats in association with that phrase.  It also produces a "total mentions" for the date range.

from sunlight import capitolwords
import json
import urllib
import wordcloud

## user defined
phrase = 'Contraception'  ## Always capitalize
start_date = '2011-01-01'
end_date = '2013-03-25'

# create API query
SUNLIGHT_API_KEY = 'f89fac39e3ef41b3b66d5ea8d86063aa'
BASE_URL = 'http://capitolwords.org/api/1/text.json?'
query = BASE_URL+'phrase={phrase}&start_date={start_date}&end_date={end_date}&party={party}&granularity=month&apikey={SUNLIGHT_API_KEY}'

# function to query and print to file
def query_and_print(partyname,filename,query,phrase):
	party = partyname
	query = query.format(phrase=phrase, start_date=start_date, end_date=end_date, party=party,SUNLIGHT_API_KEY=SUNLIGHT_API_KEY)
	data = urllib.urlopen(query).read()
	results = json.loads(data)
	resultfile = open(filename, 'w')
	for result in results['results']:
		for speaking in result['speaking']:
			speaking = remove_words(speaking)
			resultfile.write(speaking)
	resultfile.close()

def remove_words(speaking):
	speaking = speaking.replace(phrase,"") # Get rid of instances of the phrase, otherwise they'll dominate the word cloud			
	speaking = speaking.replace(phrase.lower(),"") # also get rid of lower case instances
	# Get rid of other common but not useful words, such as Mr./Ms. Speaker, and People
	speaking = speaking.replace("people","") 			
	speaking = speaking.replace("Speaker","") 			
	speaking = speaking.replace("Mr","") 			
	speaking = speaking.replace("Ms","") 			
	return speaking

# Run function to create files for word cloud
query_and_print('D','demfile.txt',query,phrase)
query_and_print('R','repfile.txt',query,phrase)

# feed these files into the word cloud program
wordcloud.main('repfile.txt')
wordcloud.main('demfile.txt')
