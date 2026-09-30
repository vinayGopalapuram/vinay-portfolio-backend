"""rename certification issue date column

Revision ID: edcd4de6d7b3
Revises: 380fece3c3f2
Create Date: 2026-09-22 15:13:10.831082

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'edcd4de6d7b3'
down_revision: Union[str, Sequence[str], None] = '380fece3c3f2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column(
        "certification",
        "issue_data",
        new_column_name="issue_date",
    )

def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column(
        "certification",
        "issue_date",
        new_column_name="issue_data",
    )
