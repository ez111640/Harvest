from .db import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from .db import db, environment, SCHEMA, add_prefix_for_prod
from .pin_to_board import pins_to_boards



class Pin(db.Model, UserMixin):
    __tablename__ = 'pins'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    boardId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("boards.id")))
    url = db.Column(db.String(40), nullable=False)
    link = db.Column(db.String())
    description = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(40), nullable=False)

    boards = db.relationship("Board", back_populates="pins")
    pin_boards= db.relationship(
        "Board",
        secondary=pins_to_boards,
        back_populates="board_pins"
    )


    def to_dict(self):
        return {
            'id': self.id,
            'boardId': self.boardId,
            'url': self.url,
            'description': self.description,
            'title': self.title
        }
