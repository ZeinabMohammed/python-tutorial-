import webbrowser
import time
breaks=3
count=0
print "This program ctarts at "+ time.ctime()
while (count<breaks):
	webbrowser.open("http://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/functions.html")
	time.sleep(10)
	count=count+1
