"""shot data

Revision ID: 844a54f803fe
Revises: 59cfe08874ca
Create Date: 2024-12-02 23:55:26.067599

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '844a54f803fe'
down_revision: Union[str, None] = '59cfe08874ca'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ShotData',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('game_id', sa.String(), nullable=False),
    sa.Column('team_id', sa.String(), nullable=False),
    sa.Column('team_name', sa.String(), nullable=False),
    sa.Column('player_id', sa.String(), nullable=False),
    sa.Column('player_name', sa.String(), nullable=False),
    sa.Column('shot_class', sa.String(), nullable=False),
    sa.Column('shot_chance', sa.Integer(), nullable=False),
    sa.Column('skill_rate', sa.Integer(), nullable=False),
    sa.Column('quality_rate', sa.Integer(), nullable=False),
    sa.Column('defender_id', sa.String(), nullable=False),
    sa.Column('defender_name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ShotData')
    # ### end Alembic commands ###