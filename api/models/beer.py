from datetime import datetime
from api.models.db import db

class Beer(db.Model):
    __tablename__ = 'beers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    style = db.Column(db.String(100))
    brewery = db.Column(db.String(100))
    location = db.column(db.String(25))
    description = db.Column(db.String(250))
    abv = db.Column(db.String(5))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id'))

    tastings = db.relationship("Tasting", cascade='all')

    def __repr__(self):
      return f"Beer('{self.id}', '{self.name}'"

    def serialize(self):
      beer = {c.name: getattr(self, c.name) for c in self.__table__.columns}
      tastings = [tasting.serialize() for tasting in self.tastings]
      beer['tastings'] = tastings
      return beer