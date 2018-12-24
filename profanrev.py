#import os
import urllib
def read_text():
	quates=open("F:\New folder (2)\movie-quotes\movie_quotes\movie_quotes.txt")
	content=quates.read()
	print content
	quates.close()
	check_profanity(content)

def check_profanity(text_to_check):
	
	connection=urllib.urlopen("http://www.wdylike.appspot.com/?q=text_to_check")
	output=connection.read()
	print output
	if "true" in output:
		print "prof error"
	elif "false"in output:
		print "no curse"
	else:
		print "i am not sure"
	connection.close()


read_text()