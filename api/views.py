from flask import Flask, jsonify, request
import datetime
# from models.models import User
# from models.models import Users


app = Flask(__name__)

users=[
{
	"id":1,
	"firstname":"bash",
	"lastname":"man",
	"othernames":"bsb",
	"email":"bash@gmail.com",
	"phoneNumber":298378,
	"registered":"3/4/2018",
	"isAdmin":1
}
]

incidents=[
{
	"iid":1,
	"createOn":"2/11/2018",
	"createdBy":1,
	"type":"red-flag",
	"location":"5464556,787788",
	"status":"under investigation",
	"Image":"image.jpg",
	"video":"video.mp4",
	"comment":"This has occured several times"
}
]


@app.route('/')
def index():
	return jsonify(['Hello World flask!'])

@app.route('/api/v1/users', methods=['POST'])
def add_user():
	data = request.get_json()
	iid = len(users)+1
	firstname = data.get('firstname')
	lastname = data.get('lastname')
	othernames = data.get('othernames')
	email = data.get('email')
	phoneNumber = data.get('phoneNumber')
	registered = data.get('registered')
	isAdmin = data.get('isAdmin')

	user = dict(iid=iid,firstname=firstname,lastname=lastname,othernames=othernames,email=email,phoneNumber=phoneNumber,registered=registered,isAdmin=isAdmin)

	users.append(user)
	return jsonify({'users':user,'message':'Success'}),200

@app.route('/api/v1/users', methods=['GET'])
def get_all_users():
	return jsonify({'users':users,'message':'Success'})
	# return jsonify({'message':'Success'})


@app.route('/api/v1/incident', methods=['POST'])
def create_incident():

	date = datetime.datetime.now()
	# date_format = str(date.day) + "/" str(date.month) + "/"+ str(date.year) 


	data = request.get_json()
	iid = len(incidents)+1
	createOn = str(date),
	createdBy = data.get('createdBy')
	type = data.get('type')
	location = data.get('location')
	status = data.get('status')
	image = data.get('image')
	video = data.get('video')
	comment = data.get('comment')

	incident = dict(iid=iid,createOn=str(date),createdBy=createdBy,type=type,location=location,status=status,image=image,video=video,comment=comment)

	incidents.append(incident)
	return jsonify({"status":200,"data":incident})


@app.route('/api/v1/red-flags', methods=['GET'])
def get_all_incidents():
	return jsonify({"status":200,"incidents":incidents}), 200



@app.route('/api/v1/red-flags/<int:redFlagId>',methods=['GET'])
def get_specific_redflag(redFlagId):
	for incident in incidents:
		if incident.get('iid') == redFlagId:
			# return jsonify({"status":200,"red-flag":incident})
			return jsonify({"message":"Sorry there are no red-flags!"})



@app.route('/api/v1/red-flags/<int:redFlagId>', methods=['DELETE'])
def delete_incident(redFlagId):
	return jsonify({"message":"Deleted"})
	


# class Users:
# 	def __init__(self,id,firstname,lastname,othernames,email,phoneNumber,registered,isAdmin):
# 		self.id = id
# 		self.firstname = firstname
# 		self.lastname = lastname
# 		self.othernames = othernames
# 		self.email = email
# 		self.phoneNumber = phoneNumber
# 		self.registered = registered



