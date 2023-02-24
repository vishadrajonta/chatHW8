#https://flask.palletsprojects.com/en/2.2.x/quickstart/#a-minimal-application
# https://www.tutorialspoint.com/flask/flask_variable_rules.htm

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross domain requests

messageDict = {}

@app.route("/chat/join/<name>")
def join(name):
	if name in messageDict:
		result = "{\"status\":\"exists\"}"
		return result
	messageDict[name] = []
	result = "{\"status\":\"success\",\"user\":\"" + name + "\"}"
	return result

@app.route("/chat/send/<name>/<message>")
def send(name,message):	
	if name not in messageDict:
		result = "{\"status\":\"baduser\"}";
		return result

	# iterate through users adding message to each
	jsonMessage = "{\"user\":\""+name+"\",\"message\":\""+message+"\"}"
	for n in messageDict:
		messageDict[n].append(jsonMessage)
	result = "{\"status\":\"success\"}"
	return result
	
@app.route("/chat/fetch/<name>")
def fetch(name):
	if name not in messageDict:
		result = "{\"status\":\"baduser\"}"
	result = "{\"messages\":[";
	first = True
	for message in messageDict[name]:
		if (not first):
			result += ",";
		result += message;
		first = False;
	result += "]}";
	messageDict[name]=[]
	return result;	
	
@app.route("/")
def about():
  return "Chat API Python"
