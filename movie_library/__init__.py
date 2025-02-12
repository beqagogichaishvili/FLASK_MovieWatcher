import os
from flask import Flask
from dotenv import load_dotenv
from pymongo import MongoClient

from movie_library.routes import pages

load_dotenv()



app = Flask(__name__)
app.config["MONGODB_URI"] = os.environ.get("MONGODB_URI")
app.config["SECRET_KEY"] = os.environ.get(
    "SECRET_KEY", "pf9Mkove5IKEAXvy-cQkeDPhv9Cb3Ag-wyJILbq_dFw"
)
app.db = MongoClient(os.environ.get("MONGODB_URI")).FLASK_MovieWatcher


app.register_blueprint(pages)
if __name__ == "__main__":
    app.run(debug=True)

