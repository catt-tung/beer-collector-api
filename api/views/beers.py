from flask import Blueprint, jsonify, request
from api.middleware import login_required, read_token

from api.models.db import db
from api.models.beer import Beer

beers = Blueprint('beers', 'beers')

@beers.route('/', methods=["POST"])
@login_required
def create():
  data = request.get_json()
  profile = read_token(request)
  data["profile_id"] = profile["id"]
  beer = Beer(**data)
  db.session.add(beer)
  db.session.commit()
  return jsonify(beer.serialize()), 201

#index beers
@beers.route('/', methods=["GET"])
def index():
  beers = Beer.query.all()
  return jsonify([beer.serialize() for beer in beers]), 200

#show a beer
@beers.route('/<id>', methods=["GET"])
def show(id):
  beer = Beer.query.filter_by(id=id).first()
  beer_data = beer.serialize()
  return jsonify(beer=beer_data), 200

#update a beer
@beers.route('/<id>', methods=["PUT"]) 
@login_required
def update(id):
  data = request.get_json()
  profile = read_token(request)
  beer = Beer.query.filter_by(id=id).first()

  if beer.profile_id != profile["id"]:
    return 'Forbidden', 403

  for key in data:
    setattr(beer, key, data[key])

  db.session.commit()
  return jsonify(beer.serialize()), 200

#delete a beer
@beers.route('/<id>', methods=["DELETE"]) 
@login_required
def delete(id):
  profile = read_token(request)
  beer = Beer.query.filter_by(id=id).first()

  if beer.profile_id != profile["id"]:
    return 'Forbidden', 403

  db.session.delete(beer)
  db.session.commit()
  return jsonify(message="Success"), 200