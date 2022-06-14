from app import myapp_obj
from flask import render_template, request

@myapp_obj.route("/")
def index():
    return render_template('index.html')

@myapp_obj.route("/process_signal", methods = ['POST'])
def process_signal():
	hz1 = request.form.get("hz1")
	hz2 = request.form.get("hz2")

	print(f'hz1:{hz1}hz2:{hz2}')

	return render_template('index.html')
