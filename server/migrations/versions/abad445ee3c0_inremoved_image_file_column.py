"""Inremoved image file column.

Revision ID: abad445ee3c0
Revises: 7aae19969427
Create Date: 2023-10-08 11:21:59.098993

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'abad445ee3c0'
down_revision = '7aae19969427'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('image_file')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_file', sa.VARCHAR(length=20), nullable=False))

    # ### end Alembic commands ###