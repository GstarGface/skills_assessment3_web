from flask import Flask, request
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index_page():
    # Return this as a strange
    return "<html><body>This is the homepage.</body></html>"

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")

@app.route("/application-form")
def application_form_page():
	return render_template("application-form.html")

@app.route("/application", methods=["GET", "POST"])
def application_page():
	firstname = request.form.get("firstname")
	lastname = request.form.get("lastname")
	salary = request.form.get("salary")
	position = request.form.get("position")
	return render_template("application-received.html", firstname=firstname, lastname=lastname, position=position, salary=salary)


if __name__ == "__main__":
    app.run(debug=True)