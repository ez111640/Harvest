from flask import Blueprint
from ..models.pin import Pin
import json

pin_routes = Blueprint("pins", __name__)

@pin_routes.route("")
def get_all_pins():
    """
    LANDING PAGE
    """
    all_pins = Pin.query.all()
    response = [pin.to_dict() for pin in all_pins]

    print("get_all_pins response", json.dumps(response))

    return json.dumps(response)


@pin_routes.route("/<int:id>")
def get_pin_details(id):
    """
    return details for a single pin by pin Id
    """
    print('##############ID', id)
    pin = Pin.query.filter(Pin.id == id).one()

    response = pin.to_dict()
    return json.dumps(response)
