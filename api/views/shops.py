from flask import Blueprint, jsonify, request
from api.middleware import login_required, read_token

from api.models.db import db
from api.models.shop import Shop

shops = Blueprint('shops', 'shops')

# create a toy
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