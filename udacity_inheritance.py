class parent():
	def __init__(self ,last_name,eye_color):
		print("parent constructor called")
		self.last_name=last_name
		self.eye_color=eye_color
	def shoe_info(self):
		print ("last_name " + self.last_name)
		print ("eye color  "+ self.eye_color)
class child(parent):
	def __init__(self,last_name,eye_color, number_of_toys):
		parent.__init__(self,last_name,eye_color)
		print "child constructor called"
		self.number_of_toys=number_of_toys
	def shoe_info(self):
		print"last name-" +self.last_name
		print "eye color -"+ self.eye_color
		print "numer of toys-" + str(self.number_of_toys)
billey_cyrus = parent ("cyrus" , "blue")
#print billey_cyrus.last_name
mily_syrus=child("cyrus","green", 5)
#print mily_syrus.number_of_toys
#print mily_syrus.eye_color
mily_syrus.shoe_info()
