#/bin/python


from subprocess import call
import shlex # For escaping the titles.

import sys # For getting the URL
url = str(sys.argv[1]) # URL is supposed to be trusted
# "https://www.reddit.com/r/spacex/new/.rss"

import feedparser
d = feedparser.parse(url) # Init parser and download the feed
filename = shlex.quote(d.feed.tags[0].term) # Get subreddit name and escape it

import dbm
with dbm.open(filename+'.db','c') as db: # Open DBM for reading writing or create it if it does not exsist.
	for entry in d.entries: # Iterate entries
		if db.get(entry.id,False): # If key entry.id does not exsist in db it will return False
			# print ("It exists")
			if db[entry.id] == bytes(entry.updated,'utf-8'): #DBM stores it as bytes so we need to compare string (entry.updated) as bytes
				# print ("It is up to date")
				continue
		# Send out notification for the user lasting 10 seconds that is MAX 64 characters long
		title = entry.title[:64]
		title = shlex.quote(title) # escape the title
		call(["notify-send", filename, title, "-t","10000"])
		# print (entry.title)
		db[entry.id] = entry.updated
		# Remember that entry was read
		pass
	db.sync() # Sync the DBM to file
	db.close() # Technically this also syncs it so... idk why am I doin the previous line
exit()
