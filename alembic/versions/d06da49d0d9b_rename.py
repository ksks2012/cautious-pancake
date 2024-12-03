"""rename

Revision ID: d06da49d0d9b
Revises: 844a54f803fe
Create Date: 2024-12-03 21:32:07.958330

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd06da49d0d9b'
down_revision: Union[str, None] = '844a54f803fe'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - adjusted for renaming columns ###

    # Rename `skill_rate` to `skills_ratio`
    op.alter_column('ShotData', 'skill_rate', new_column_name='skills_ratio')

    # Rename `quality_rate` to `shot_quality`
    op.alter_column('ShotData', 'quality_rate', new_column_name='shot_quality')

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - adjusted for reverting renaming columns ###

    # Rename `skills_ratio` back to `skill_rate`
    op.alter_column('ShotData', 'skills_ratio', new_column_name='skill_rate')

    # Rename `shot_quality` back to `quality_rate`
    op.alter_column('ShotData', 'shot_quality', new_column_name='quality_rate')

    # ### end Alembic commands ###
