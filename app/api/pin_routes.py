from flask import Blueprint, request
from ..models.pin import Pin
import json
from ..forms.pin_form import PinForm
from flask_login import login_required, current_user # current_user.id
from ..models import db

pin_routes = Blueprint("pins", __name__)


@pin_routes.route("/<int:id>")
def get_pin_details(id):
    """
    return details for a single pin by pin Id
    """
    print('##############ID', id)
    pin = Pin.query.filter(Pin.id == id).one()

    response = pin.to_dict()
    return json.dumps(response)

@pin_routes.route("")
def get_all_pins():
    """
    LANDING PAGE
    """
    all_pins = Pin.query.all()
    response = [pin.to_dict() for pin in all_pins]

    print("get_all_pins response", json.dumps(response))

    return json.dumps(response)


@pin_routes.route("", methods=["POST"])
def add_new_pin():
    """
    ADD A NEW PIN
    """
    form = PinForm()
    form["csrf_token"].data = request.cookies["csrf_token"]

    if form.validate_on_submit ():
        pin = Pin(
            url = form.data["url"],
            link=form.data["link"],
            description=form.data["description"],
            title = form.data["title"],
            creatorId = current_user.id
        )

        db.session.add(pin)
        db.session.commit()

    return pin.to_dict()


@pin_routes.route("/<int:id>", methods=["PUT"])
def update_review(id):
    """
    Post new review for product by product id
    """
    form = PinForm()
    form["csrf_token"].data = request.cookies["csrf_token"]
    pin = Pin.query.get(id)
    if form.validate_on_submit():
            pin.url = form.data["url"],
            pin.link=form.data["link"],
            pin.description=form.data["description"],
            pin.title = form.data["title"],
            pin.creatorId = current_user.id
            print("REVIEW", pin)
            db.session.commit()
            return pin.to_dict()
    else:
          print(form.errors)
          return {"errors":form.errors}
