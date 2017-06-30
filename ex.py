from flask import Flask, render_template, request
from flask import jsonify

app= Flask(__name__)

@app.route('/')

def home():
	return render_template('form.html')

@app.route('/searchb',methods= ['POST', 'GET'])

def search():
	if request.method == 'POST':
		form_inp = request.form['inp']
 	z= result(form_inp)
 	if not z:
 		return "Your search didnt match with any course !"
 	else:
 		return jsonify(branch=z)



@app.route('/searchc',methods= ['POST', 'GET'])

def searchc():
	if request.method == 'POST':
		form_inp = request.form['inp']
 	li= resultc(form_inp)
 	if not li:
 		return "Your search didnt match with any university !"
 	else:
 		return jsonify(University=li)




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

def result(form_inp):
	k=[]
	for y in a:
		for z in y["course"]:
			str1=z["name"]
			if str(form_inp).upper() in str1:
				k.append(z)
	return k
	


def resultc(form_inp):
	l=[]
	for y in a:
		str1=y["name"]
		if str(form_inp).upper() in str1:
			l.append(y)
	return l
	



if __name__ == '__main__':
	app.run()
