from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
	return "Hello World! It is updated to test the Jenkins pipeline on EC2 instance. (V2)"
