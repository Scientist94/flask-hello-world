#importing Flask class from flask module
from flask import Flask

#create application process
app = Flask(__name__)

#error handling
app.config["DEBUG"] = True

#using decorators
@app.route("/")
@app.route("/hello")

#define view using function, which returns a string
def hello_world():
	return "hello WOrld!!"

#dynamic route
@app.route("/test/<search_query>")
def search(search_query):
	return search_query

#dynamic route with explicit status code
@app.route("/name/<name>")
def index(name):
	if name.lower() == "michael":
		return "hello, {}".format(name)
	else:
		return "404: Not fucking Found", 404

#start server using run() method
if __name__ == "__main__" :
	app.run()

