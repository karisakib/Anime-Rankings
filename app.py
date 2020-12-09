from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///anime.db'

db = SQLAlchemy(app)

class AnimeTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rank = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(255), nullable=False)
    rating = db.Column(db.String(255), nullable=False)
    link = db.Column(db.String(255), nullable=False)

@app.route("/", methods=["GET"])
def homoe():
    table = AnimeTable.query.all()
    d=[]
    for row in table:
        row_as_dict = {
            "rank": row.rank,
            "title": row.title,
            "rating": row.rating,
            "link": row.link,
        }
        d.append(row_as_dict)
    return render_template("home.html", data = d)

if __name__ == '__main__':
    app.run(debug=True)

@app.route("/api", methods=["GET"])
def api_route():
    table = AnimeTable.query.all()
    d=[]
    for row in table:
        row_as_dict = {
            "rank": row.rank,
            "title": row.title,
            "rating": row.rating,
            "link": row.link,
        }
        d.append(row_as_dict)
    return jsonify(d)

if __name__ == '__main__':
    app.run(debug=True)