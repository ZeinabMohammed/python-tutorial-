import random
import math, datetime, calendar
import os

cources = ['history', 'math', 'physics', 'compsci']
random_cources = random.choice(cources)
print (random_cources)


rads= math.radians(90)
print (math.sin(rads))


today = datetime.date.today()
print (today)
print (calendar.isleap(2017))

print (os.getcwd())
print (os.__file__) #entire standard library path




