from .db import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from .db import db, environment, SCHEMA, add_prefix_for_prod


pins_to_likes = db.Table(
    "pins-to-likes",
    db.Modal.metadata,
    db.Column("pin_id", db.Integer, db.ForeignKey("pins.id"), primary_key=True),
    db.Column("board_id", db.Integer, db.ForeignKey("boards.id", primary_key=True))
)
