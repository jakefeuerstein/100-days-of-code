from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy, query
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

# with app.app_context():
#     db.create_all()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random", methods=['GET'])
def get_random_cafe():
    # if request.data:
    cafes = db.session.query(Cafe).all()
    ran_cafe = random.choice(cafes)
    return jsonify(cafe=ran_cafe.to_dict())

@app.route("/all", methods=['GET'])
def get_all_cafes():
    all_cafes = db.session.query(Cafe).all()
    all_cafes_dict = [cafe.to_dict() for cafe in all_cafes]
    return jsonify(all_cafes=all_cafes_dict)

@app.route("/search", methods=['GET'])
def search():
    search_area = request.args.get("loc")
    cafe = db.session.query(Cafe).filter_by(location=search_area).first()
    if cafe:
        print(cafe)
        return jsonify(matching_cafe=cafe.to_dict())
    return {'error': {
            'Not Found': "Sorry, we don't have a cafe at that location"}
    }

@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        cafe = Cafe(
            name=request.form.get("name"),
            map_url=request.form.get("map_url"),
            img_url=request.form.get("img_url"),
            location=request.form.get("location"),
            seats=request.form.get("seats"),
            has_toilet=bool(request.form.get("has_toilet")),
            has_wifi=bool(request.form.get("has_wifi")),
            has_sockets=bool(request.form.get("has_sockets")),
            can_take_calls=bool(request.form.get("can_take_calls")),
            coffee_price=request.form.get("coffee_price")
        )

        db.session.add(cafe)
        db.session.commit()
        return {'response': {'success': "Successfully added the new cafe"}}
    return {'response': {'failure': "Failed to add the new cafe"}}

@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    if request.method == "PATCH":
        Cafe.query.filter_by(id=cafe_id).update(coffee_price=request.args.get("coffee_price"))
        db.session.commit()
        return {'response': {'success': "Successfully added the new cafe"}}
    return {'response': {'failure': "Failed to add the new cafe"}}

@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def report_closed(cafe_id):
    cafe = Cafe.query.filter_by(id=cafe_id)
    if cafe:
        if request.args.get("api_key") == 'TOPSECRETKEY':
            cafe.delete()
            db.session.commit()
            return jsonify(response={'success': "Successfully deleted the cafe"})
        return jsonify(response={'Forbidden': "Incorrect api key"}), 403
    return jsonify(response={'Not Found': "Cafe does not exist"}), 404


if __name__ == '__main__':
    app.run(debug=True)
