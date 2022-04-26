from datetime import datetime
from api.models.db import db

class Tasting(db.Model):
    __tablename__ = 'tastings'
    id = db.Column(db.Integer, primary_key=True)
    shop = db.Column(db.String(100))
    impressions = db.Column(db.String(350))
    date = db.Column(db.DateTime, default=datetime.now(tz=None))
    created_at = db.Column(db.DateTime, default=datetime.now(tz=None))
    beer_id = db.Column(db.Integer, db.ForeignKey('beers.id'))

    def __repr__(self):
      return f"Tasting('{self.id}', '{self.shop}'"

    def serialize(self):
      return {
        "id": self.id,
        "shop": self.shop,
        "impressions": self.impressions,
        "beer_id": self.beer_id,
        "date": self.date.strftime('%Y-%m-%d'),
      }
