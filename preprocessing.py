from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///shoes.db"
db = SQLAlchemy(app)


class Shoe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(), nullable=False)
    name = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    price = db.Column(db.Float(5, 2), nullable=False)
    color = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return "<Product %r>" % self.id


def convertJsonToDb():
    with open("./static/data/shoes.json", "r") as file:
        shoes_data = json.load(file)

        for shoe_data in shoes_data["shoes"]:
            shoe = Shoe(
                id=shoe_data["id"],
                image=shoe_data["image"],
                name=shoe_data["name"],
                description=shoe_data["description"],
                price=shoe_data["price"],
                color=shoe_data["color"],
            )
            db.session.add(shoe)
        db.session.commit()


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        convertJsonToDb()
