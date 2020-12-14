from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_trulia

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/trulia_app"
mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/craigslist_app")


@app.route("/")
def index():
    houses = mongo.db.houses.find_one()
    return render_template("index.html", houses=houses)


@app.route("/scrape")
def scraper():
    houses = mongo.db.houses
    houses_data = scrape_trulia.scrape()
    houses.update({}, houses_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
