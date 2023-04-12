"""many to many relation

Revision ID: 08ef690a745d
Revises: 26abac199264
Create Date: 2023-04-11 12:41:15.677837

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '08ef690a745d'
down_revision = '26abac199264'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cookie_order',
    sa.Column('cookie_id', sa.Integer(), nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.Column('number_of_cookies', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cookie_id'], ['cookie.id'], ),
    sa.ForeignKeyConstraint(['order_id'], ['order.id'], ),
    sa.PrimaryKeyConstraint('cookie_id', 'order_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cookie_order')
    # ### end Alembic commands ###