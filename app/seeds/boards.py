from app.models import db, Board


def seed_boards():
    board1 = Board(
        userId='1', name='Gardening'
    )
    board2 = Board(
        userId='2', name='Gardening'
    )
    board3 = Board(
        userId='3', name='Gardening'
    )
    board4 = Board(
        userId='4', name='Gardening'
    )
    board5 = Board(
        userId='5', name='Woodworking'
    )
    board6 = Board(
        userId='6', name='Woodworking'
    )
    board7 = Board(
        userId='7', name='Cooking'
    )
    board8 = Board(
        userId='8', name='Cooking'
    )

    db.session.add(board1)
    db.session.add(board2)
    db.session.add(board3)
    db.session.add(board4)
    db.session.add(board5)
    db.session.add(board6)
    db.session.add(board7)
    db.session.add(board8)

def undo_boards():
    db.session.execute('TRUNCATE boards RESTART IDENTITY CASCADE;')
    db.session.commit()
