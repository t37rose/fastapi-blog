"""empty message

Revision ID: 832eecb5dfb8
Revises: f14f46e341fc
Create Date: 2021-02-09 12:02:01.852587

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '832eecb5dfb8'
down_revision = 'f14f46e341fc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('body', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'body')
    # ### end Alembic commands ###
