"""Initial Migration

Revision ID: 3b1507b19719
Revises: 
Create Date: 2023-12-09 12:27:31.510112

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3b1507b19719'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    
    op.create_table('restaurants',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name',sa.String(), nullable=False),
        sa.Column('price', sa.Integer(), nullable=False),

        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint('name'),
        )
    
    op.create_table('customers',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('first_name', sa.String(), nullable=False),
        sa.Column('last_name', sa.String(), nullable=False),

        sa.PrimaryKeyConstraint('id'),
        )
    
    op.create_table('reviews',
            sa.Column('id', sa.Integer(), nullable=False),
            sa.Column('star_rating', sa.Integer(), nullable=False),
            sa.Column('restaurant_id', sa.Integer(), sa.ForeignKey('restaurants.id'),nullable=False),
            sa.Column('customer_id', sa.Integer(), sa.ForeignKey('customers.id'),nullable=False),

            sa.PrimaryKeyConstraint('id')
        )


def downgrade() -> None:
    pass
