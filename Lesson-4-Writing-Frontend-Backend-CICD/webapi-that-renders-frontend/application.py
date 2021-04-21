from flask import Flask, render_template

#  __name__ is just a convenient way to get the import name of the place the app is defined.
# Flask uses the import name to know where to look up resources, templates, static files, instance folder, etc
application = Flask(__name__)

@application.route("/")
def home():
    return render_template('index.html')

# For local use only
# application.run(host='127.0.0.1', port='5000')

# For the cloud
application.run(host='0.0.0.0', port='5000')