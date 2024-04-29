"""Modification des certaines champs

Revision ID: 6ef36b9f39a2
Revises: 1ed58313e799
Create Date: 2024-04-08 16:56:16.716287

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6ef36b9f39a2'
down_revision: Union[str, None] = '1ed58313e799'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
