"""empty message

Revision ID: 12e45f740be6
Revises: dbcacf627fec
Create Date: 2023-09-06 12:30:35.982701

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12e45f740be6'
down_revision = 'dbcacf627fec'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_column('comments', 'commentText')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('commentText', sa.VARCHAR(length=255), nullable=False))
    op.create_foreign_key(None, 'comments', 'pins', ['pinId'], ['id'])
    # ### end Alembic commands ###