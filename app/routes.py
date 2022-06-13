from app import myapp_obj
from flask import render_template

@myapp_obj.route("/")
def index():
    	return render_template('index.html')
