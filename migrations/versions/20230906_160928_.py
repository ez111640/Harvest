"""empty message

Revision ID: b64d92c17141
Revises:
Create Date: 2023-09-06 16:09:28.660398

"""
from alembic import op
import sqlalchemy as sa

import os
environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")


# revision identifiers, used by Alembic.
revision = 'b64d92c17141'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('topics',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=40), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    if environment == "production":
        op.execute(f"ALTER TABLE topics SET SCHEMA {SCHEMA};")
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.Column('firstName', sa.String(length=40), nullable=True),
    sa.Column('lastName', sa.String(length=40), nullable=True),
    sa.Column('city', sa.String(length=40), nullable=True),
    sa.Column('state', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    if environment == "production":
        op.execute(f"ALTER TABLE users SET SCHEMA {SCHEMA};")
    op.create_table('boards',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    if environment == "production":
        op.execute(f"ALTER TABLE boards SET SCHEMA {SCHEMA};")
    op.create_table('follows',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=True),
    sa.Column('topicId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['topicId'], ['topics.id'], ),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    if environment == "production":
        op.execute(f"ALTER TABLE follows SET SCHEMA {SCHEMA};")
    op.create_table('pins',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(), nullable=False),
    sa.Column('link', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('creatorId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['creatorId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    if environment == "production":
        op.execute(f"ALTER TABLE pins SET SCHEMA {SCHEMA};")
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=True),
    sa.Column('pinId', sa.Integer(), nullable=False),
    sa.Column('commentText', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['pinId'], ['pins.id'], ),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    if environment == "production":
        op.execute(f"ALTER TABLE comments SET SCHEMA {SCHEMA};")
    op.create_table('pins_to_boards',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pinId', sa.Integer(), nullable=True),
    sa.Column('boardId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['boardId'], ['boards.id'], ),
    sa.ForeignKeyConstraint(['pinId'], ['pins.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    if environment == "production":
        op.execute(f"ALTER TABLE pins_to_boards SET SCHEMA {SCHEMA};")
    op.create_table('topics_to_boards',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('topicId', sa.Integer(), nullable=True),
    sa.Column('boardId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['boardId'], ['boards.id'], ),
    sa.ForeignKeyConstraint(['topicId'], ['topics.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    if environment == "production":
        op.execute(f"ALTER TABLE topics_to_boards SET SCHEMA {SCHEMA};")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('topics_to_boards')
    op.drop_table('pins_to_boards')
    op.drop_table('comments')
    op.drop_table('pins')
    op.drop_table('follows')
    op.drop_table('boards')
    op.drop_table('users')
    op.drop_table('topics')
    # ### end Alembic commands ###
