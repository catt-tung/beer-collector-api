from datetime import datetime
from api.models.db import db

class Shop(db.Model):
    __tablename__ = 'shops'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    location = db.Column(db.String(250))
    vibe = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id'))

    def __repr__(self):
      return f"Shop('{self.id}', '{self.name}'"

    def serialize(self):
      shop = {c.name: getattr(self, c.name) for c in self.__table__.columns}
      return shop