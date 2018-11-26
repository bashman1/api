users=[]

class Users:
	def __init__(self,id,firstname,lastname,othernames,email,phoneNumber,registered,isAdmin):
		self.id = id
		self.firstname = firstname
		self.lastname = lastname
		self.othernames = othernames
		self.email = email
		self.phoneNumber = phoneNumber
		self.registered = registered