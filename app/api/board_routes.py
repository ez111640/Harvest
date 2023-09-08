from flask import Blueprint
from ..models.board import Board
from ..models.pin_to_board import Pins_To_Boards
from ..models.pin import Pin
from flask_login import current_user, login_required
import json

board_routes = Blueprint("boards", __name__)

@board_routes.route("")
def get_user_boards():
    """
    Main user page listing all user boards
    """
    user_boards = Board.query.filter(Board.userId == current_user.id).all()
    response = [board.to_dict() for board in user_boards]


    print("get_user_boards response", json.dumps(response))

    return json.dumps(response)


@board_routes.route("/<int:id>/pins")
def get_board_pins(id):
    """
    get all pins by board
    """
    print("ID", id)
    pins_to_boards = Pins_To_Boards.query.filter(Pins_To_Boards.boardId == id)
    response = [ptb.to_dict() for ptb in pins_to_boards]

    return json.dumps(response)
