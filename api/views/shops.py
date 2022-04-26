from flask import Blueprint, jsonify, request
from api.middleware import login_required, read_token

from api.models.db import db
from api.models.shop import Shop

shops = Blueprint('shops', 'shops')

# create a shop
@shops.route('/', methods=["POST"]) 
@login_required
def create():
  data = request.get_json()
  profile = read_token(request)
  data["profile_id"] = profile["id"]

  shop = Shop(**data)
  db.session.add(shop)
  db.session.commit()
  return jsonify(shop.serialize()), 201

# index shops
@shops.route('/', methods=["GET"])
def index():
  shops = Shop.query.all()
  return jsonify([shop.serialize() for shop in shops]), 201

# show a shop
@shops.route('/<id>', methods=["GET"])
def show(id):
  shop = Shop.query.filter_by(id=id).first()
  return jsonify(shop.serialize()), 200

# update a shop
@shops.route('/<id>', methods=["PUT"]) 
@login_required
def update(id):
  data = request.get_json()
  profile = read_token(request)
  shop = Shop.query.filter_by(id=id).first()

  if shop.profile_id != profile["id"]:
    return 'Forbidden', 403

  for key in data:
    setattr(shop, key, data[key])

  db.session.commit()
  return jsonify(shop.serialize()), 200

# delete a shop
@shops.route('/<id>', methods=["DELETE"]) 
@login_required
def delete(id):
  profile = read_token(request)
  shop = Shop.query.filter_by(id=id).first()

  if shop.profile_id != profile["id"]:
    return 'Forbidden', 403
    
  db.session.delete(shop)
  db.session.commit()
  return jsonify(message="Success"), 200