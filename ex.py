# pre-made database (json array)

a=[
{
	"name":"JIIT","type":"private","Rank":9, "year of establish":1998, 
	"course":[
		{"name":"ELECTRONICS AND COMMUNICATION ENGINEERING","fees":50000, "duration":4},
		{"name":"COMPUTER SCIENCE ENGINEERING","fees":50000, "duration":3}
		]
},
{
"name":"IIT", "type":"public","Rank":2, "year of establish":1988, 
"course":[
		{"name":"DIPLOMA","fees":5000, "duration":4},
		{"name":"B-TECH","fees":5000, "duration":3}
		]
},

{
"name":"BITS", "type":"public","Rank":2, "year of establish":1988, 
"course":[
		{"name":"M.B.A.","fees":500000, "duration":4},
		{"name":"M-TECH","fees":50000, "duration":3}
		]
},
{
"name":"NIT", "type":"public","Rank":2, "year of establish":1988, 
"course":[
		{"name":"BSC","fees":5000, "duration":4},
		{"name":"BCOM","fees":5000, "duration":3}
		]
},
{
"name":"SRCC", "type":"public","Rank":2, "year of establish":1988, 
"course":[
		{"name":"BBA.","fees":5000, "duration":4},
		{"name":"BA","fees":5000, "duration":3}
		]
}
]

# import flask modules

from flask import Flask, render_template, request
from flask import jsonify

app= Flask(__name__)

#home page  http://localhost:5000/

@app.route('/')

def home():
	return render_template('form.html')

@app.route('/searchb',methods= ['POST', 'GET'])

#branch search  http://localhost:5000/searchb

def search():
	if request.method == 'POST':
		form_inp = request.form['inp']
 	output= branch_search(form_inp)
 	if not output:
 		return "Your search didnt match with any course !"
 	else:
 		return jsonify(branch=output)


#university search http://localhost:5000/searchc

@app.route('/searchc',methods= ['POST', 'GET'])

def searchc():
	if request.method == 'POST':
		form_inp = request.form['inp']
 	output= university_search(form_inp)
 	if not output:
 		return "Your search didnt match with any university !"
 	else:
 		return jsonify(University=output)


# extracting branch matching with user data from json array a

def branch_search(form_inp):
	k=[]										#locally declared list
	for y in a:									#loop in json array a
		for z in y["course"]:					#loop in a[course] , searching through course
			str1=z["name"]						# name of branch in array
			if str(form_inp).upper() in str1:	#if enter detail present in branch
				k.append(z)						#make a list of json data of branch
	return k
	

# extracting university detail matching with user data from json array a


def university_search(form_inp):
	k=[]										#locally declared list
	for y in a:									#iterate through json array
		str1=y["name"]							#copy name of university in string str1
		if str(form_inp).upper() in str1:		#if input is present in str
			k.append(y)							#append json data in list k
	return k
	



if __name__ == '__main__':
	app.run()
