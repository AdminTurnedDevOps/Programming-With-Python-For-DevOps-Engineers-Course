from flask import Flask

#  __name__ is just a convenient way to get the import name of the place the app is defined.
# Flask uses the import name to know where to look up resources, templates, static files, instance folder, etc
application = Flask(__name__)

@application.route("/")
def home():
    return "Hello CloudSkills!"