"""Added price column in the menu table.

Revision ID: d821fd64b69b
Revises: 02f3062baf2b
Create Date: 2023-10-05 16:43:24.798477

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd821fd64b69b'
down_revision = '02f3062baf2b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('menus', schema=None) as batch_op:
        batch_op.add_column(sa.Column('price', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('menus', schema=None) as batch_op:
        batch_op.drop_column('price')

    # ### end Alembic commands ###